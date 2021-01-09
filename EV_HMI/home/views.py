from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'posts': Post.objects.all()
    }
    return render(request, 'home/news.html', context)


def about(request):
    return render(request, 'home/about.html')
