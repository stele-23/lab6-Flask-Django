from django.shortcuts import render
from .models import Message

def home(request):
    return render(request, 'index.html')

def greet(request, name):
    return render(request, 'greet.html', {'name': name})

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'messages.html', {'messages': messages})
