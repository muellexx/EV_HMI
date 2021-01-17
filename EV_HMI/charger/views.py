from django.shortcuts import render


def dashboard(request):
    context = {'title': 'Dashboard', 'sidebar': 'Home'}
    return render(request, 'charger/dashboard.html', context)
