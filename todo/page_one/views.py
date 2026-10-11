from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Tasks
import datetime



def html_render(request):
    return render(request, 'todo.html')


def save_task(request):
    if request.method == 'POST':
        text = request.POST.get('task')
        Tasks.task = text
        return HttpResponse(Tasks.task)
    else:
        return HttpResponseNotAllowed(['POST'])