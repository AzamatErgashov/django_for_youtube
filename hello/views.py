from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def print_hello(request):
    return HttpResponse('hello, world')

def azamat(request):
    return HttpResponse('hello, azamat')

def akmal(request):
    return HttpResponse('hello, akmal')
