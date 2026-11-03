from django.shortcuts import render, redirect
from django import forms

tasks = ['read', 'sleep', 'coffee']


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):
    return render(request, "proectapp.html", {
        "task": tasks
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)

            return redirect("tasks:index")

    else:
        form = NewTaskForm()

    return render(request, "add.html", {
        "form": form
    })