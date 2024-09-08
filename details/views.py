from django.shortcuts import get_object_or_404, render

from details.models import Movie

# Create your views here.
def movies_detail(request,pk):
    movies=get_object_or_404(Movie,pk=pk)
    context={
        'movies':movies,
    }
    return render(request,'movies_detail.html',context)
