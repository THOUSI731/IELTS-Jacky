from django.shortcuts import render
from .models import Thumbnail,Feature

def homeview(request):
    thumbnails=Thumbnail.objects.all()
    features=Feature.objects.all()
    context={
        "thumbnails":thumbnails,
        "features":features
    }
    return render(request, "home/home.html",context)
