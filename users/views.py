from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('Hello')
    return render(request,"users/index.html", {})
