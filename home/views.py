from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Task

def home(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    
    return render(request, "home/home.html", context)

def add_task(request):
    context = {'success': False}
    if request.method=="POST":
        task_title = request.POST['task']
        task_desc = request.POST['desc']
        Task(task_title=task_title, task_desc=task_desc).save()
        context['success'] = True
                    
    return render(request, "home/add_task.html", context)

def delete_task(request, task_id):
    if request.method=="POST":
        Task.objects.filter(id=task_id).delete()
        return redirect("home")

def mark_complete(request, task_id):
    if request.method=="POST":
        task = Task.objects.get(id=task_id)
        task.status = True
        task.save()
        return redirect("home")
    
def completed_tasks(request):
    tasks = Task.objects.filter(status=True)
    context = {'tasks': tasks}
    
    return render(request, "home/completed_tasks.html", context)

def mark_incomplete(request, task_id):
    if request.method=="POST":
        task = task = Task.objects.get(id=task_id)
        task.status = False
        task.save()
        return redirect("completed_tasks")