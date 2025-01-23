from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

def index(request):
    posts = Post.objects.all()
    return render(request, 'home/index.html', {'posts': posts})

def index2(request):
    posts = Post.objects.all()
    return render(request, 'home/index2.html', {'posts': posts})

class PostListView(ListView):
    model = Post
    template_name = 'home/post_list.html'  # Your blog's template file
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'home/post_detail.html'  # A new template for the detailed view
    context_object_name = 'post'
