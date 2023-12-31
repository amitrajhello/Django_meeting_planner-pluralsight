from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting

def welcome(request):
    # return render(request, "website/welcome.html", {"num_meetings": Meeting.objects.count()})
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse('This page was served at '+ str(datetime.now()))

def about(request):
    return HttpResponse('This is the about page')

