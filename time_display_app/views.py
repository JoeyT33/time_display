from django.shortcuts import render, HttpResponse
from time import gmtime, strftime


def index(request):
    return render(request, 'time_display.html')

def time(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'time_display.html', context)