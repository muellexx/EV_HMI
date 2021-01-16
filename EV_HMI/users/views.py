from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CompanyCreateForm
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
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


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
            return redirect('profile')
    else:
        form = CompanyCreateForm()
    return render(request, 'users/company_create.html', {'form': form})


class CompanyDetailView(DetailView):
    model = Company


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
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register_employee.html', {'form': form, 'company': company})
