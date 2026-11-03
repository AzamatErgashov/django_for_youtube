from django.shortcuts import render

# Create your views here.
task = ['read','sleep','coffee']
def index(request):
    return render(request, "proectapp.html", {
         "task": task
    })