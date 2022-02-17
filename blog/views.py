from django.shortcuts import render
from django.http import HttpResponse
# from django.utils import User
from .models import Post

# Create your views here.
# posts = [
#     {
#         'title': 'Blog Post 1',
#         'author': 'Livelinks',
#         'date_posted': 'February 14, 2022',
#         'content': 'First blog post, it is gonna be awesome'
#     }, 
#     {
#         'title': 'Blog Post 2',
#         'author': 'Malik',
#         'date_posted': 'February 16, 2022',
#         'content': 'Second blog post, it is gonna be fantastic'
#     }
# ]

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})