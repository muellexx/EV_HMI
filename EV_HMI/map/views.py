from django.shortcuts import render


# Create your views here.
def map_view(request):
    context = {'title': 'Map', 'sidebar': 'Home'}
    return render(request, 'map/map.html', context)
