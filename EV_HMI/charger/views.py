from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'charger/home.html', context)


def about(request):
    return render(request, 'charger/about.html')

def dashboard(request):
    return render(request, 'charger/dashboard.html')
