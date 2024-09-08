from django.shortcuts import render

from details.models import Movie

def home(request):
    movies=Movie.objects.all()
    context={
        'movies':movies,
    }
    return render(request,'home.html',context)