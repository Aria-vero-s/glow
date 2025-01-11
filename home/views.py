from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def index(request):
    posts = Post.objects.all()
    return render(request, 'home/index.html', {'posts': posts})

def index2(request):
    posts = Post.objects.all()
    return render(request, 'home/index2.html', {'posts': posts})