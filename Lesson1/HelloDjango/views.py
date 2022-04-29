from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now=datetime.now()
        
    return render(
        request,
        "Hellodjango/index.html",
        {
          'content':"Hello Django",
          'number': now.strftime("%A, %d %B, %Y at %X")
        }
        )
# Create your views here.