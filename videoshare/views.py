from django.shortcuts import render, HttpResponse
from .models import Videos 

def home(request):
    videos = Videos.objects.all()
    print(videos)
    filtered_videos = None

    if 'filter' in request.GET:
        filter_text = request.GET['filter']
        filtered_videos = Videos.objects.filter(title__icontains=filter_text)

    context = {
        'movies': videos,
        'filtered_movies': filtered_videos,
    }

    return render(request, 'home.html', context)