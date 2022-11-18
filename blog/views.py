from django.shortcuts import render
from datetime import datetime
from blog.models import Post

from django.views.generic import ListView, DetailView, CreateView
# from django.http import HttpResponse

# Create your views here.
def home(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model=Post
    template_name = 'blog/home.html' # default: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(CreateView):
    model=Post
    fields=['title', 'content']

    def form_valid(self, form):
        # Para indicar que al momento de hacer click en "Post", tome como "author" del Post al User logeado
        form.instance.author = self.request.user
        return super().form_valid(form)



def about(request):
    return render(request, 'blog/about.html', {'title':'About'})



