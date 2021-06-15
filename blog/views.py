from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = "posts"


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = "post"


class BlogCreateView(CreateView):  # new
    model = Post
    template_name = 'blog/new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    context_object_name = "a"
    success_url = reverse_lazy('home')
