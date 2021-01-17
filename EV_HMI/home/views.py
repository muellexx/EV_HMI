from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


# def news(request):
#     context = {
#         'title': 'Home',
#         'posts': Post.objects.all()
#     }
#     return render(request, 'home/news.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'home/news.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'News'
        context['sidebar'] = 'Home'
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'News'
        context['sidebar'] = 'Home'
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Post'
        context['sidebar'] = 'Home'
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Post'
        context['sidebar'] = 'Home'
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Post'
        context['sidebar'] = 'Home'
        return context


def about(request):
    context = {'title': 'About', 'sidebar': 'Home'}
    return render(request, 'home/about.html', context)
