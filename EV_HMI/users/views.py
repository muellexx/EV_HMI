from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView, DeleteView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CompanyCreateForm, CompanyUpdateForm, GroupUpdateForm
from .models import Company, CompanyEmployee
from .decorators import user_is_authorized


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register', 'sidebar': 'Profile'})


def create_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'A new User has successfully been created!')
            return redirect('user-detail', user.pk)
    else:
        form = UserRegisterForm()
    return render(request, 'users/user_create.html', {'form': form, 'title': 'Create User', 'sidebar': 'Settings'})


@login_required
def profile(request):
    context = {'title': 'Profile', 'sidebar': 'Profile'}
    return render(request, 'users/profile.html', context)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile Edit',
        'sidebar': 'Settings',
    }
    return render(request, 'users/profile_edit.html', context)


def create_company(request):
    if request.method == 'POST':
        form = CompanyCreateForm(request.POST)
        if form.is_valid():
            group = form.save()
            company = Company(group=group)
            company.save()
            messages.success(request, f'You successfully created a new company.')
            return redirect('company-detail', company.pk)
    else:
        form = CompanyCreateForm()
    return render(request, 'users/company_create.html', {'form': form, 'title': 'Company Create', 'sidebar': 'Settings'})


class CompanyDetailView(DetailView):
    model = Company
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Company Detail'
        context['sidebar'] = 'Settings'
        return context


@user_is_authorized
def register_employee(request, pk):
    print(request.user)
    company = Company.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            company_employee = CompanyEmployee(user=user, company=company)
            company_employee.save()
            company.group.user_set.add(user)
            messages.success(request, f'You successfully added an employee')
            return redirect('user-detail', user.pk)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register_employee.html', {'form': form, 'company': company, 'title': 'Add Employee', 'sidebar': 'Settings'})


class UserDetailView(DetailView):
    model = User
    context_object_name = 'object'
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User'
        context['sidebar'] = 'Settings'
        return context


@login_required
def user_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'The User has been updated!')
            return redirect('user-detail', user.pk)

    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'object': user,
        'title': 'Profile Edit',
        'sidebar': 'Settings',
    }
    return render(request, 'users/user_edit.html', context)


@login_required
def company_edit(request, pk):
    company = Company.objects.get(pk=pk)
    if company.homepage:
        print('hi')
    if request.method == 'POST':
        g_form = GroupUpdateForm(request.POST, instance=company.group)
        c_form = CompanyUpdateForm(request.POST, request.FILES, instance=company)
        if g_form.is_valid() and c_form.is_valid():
            g_form.save()
            c_form.save()
            messages.success(request, f'The Company has been updated!')
            return redirect('company-detail', company.pk)

    else:
        g_form = GroupUpdateForm(instance=company.group)
        c_form = CompanyUpdateForm(instance=company)

    context = {
        'u_form': g_form,
        'p_form': c_form,
        'object': company,
        'title': 'Profile Edit',
        'sidebar': 'Settings',
    }
    return render(request, 'users/company_edit.html', context)


class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Company
    success_url = '/'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Company'
        context['sidebar'] = 'Settings'
        return context


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = '/'
    template_name = 'users/user_confirm_delete.html'
    context_object_name = 'object'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete User'
        context['sidebar'] = 'Settings'
        return context
