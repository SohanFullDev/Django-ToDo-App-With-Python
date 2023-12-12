#from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
   # tasks = Task.objects.filter(is_completed=False).order_by('updated_at')
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    
    completed_tasks = Task.objects.filter(is_completed=True)
    print(completed_tasks)
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html', context)