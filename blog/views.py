from msilib.schema import ListView
from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html' #  by default -> <app>/<model>_<list_type>.html
    
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4
    
    
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/index.html' #  by default -> <app>/<model>_<list_type>.html
    context_object_name = 'posts'
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        
    
    
class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

       
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content'] 
    
    # setting the post author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Ensuring that the user updating a particular post is the post creator
    def test_func(self):
        post = self.get_object()
        
        if self.request.user == post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
        
        
    # Ensuring that the user updating a particular post is the post creator
    def test_func(self):
        post = self.get_object()
        
        # Redirect here after successfull deletion of post
        
        if self.request.user == post.author:
            return True
        return False
   
   
def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})