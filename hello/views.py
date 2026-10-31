from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def print_hello(request):
    return render(request, 'main.html')

def azamat(request):
    return HttpResponse('hello, azamat')

def akmal(request):
    return HttpResponse('hello, akmal')

# def greet(request, name):
#     return HttpResponse(f'hello {name}')

def greet(request, name):
    return render(request, 'greet.html', {"name": name.capitalize()})