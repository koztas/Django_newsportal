from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView,
                                  )
from .models import *
from .filters import PostFilter
from .forms import PostForm
from django.http import HttpResponse


class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/authors.html'


class Post(DetailView):
    model = Post
    context_object_name = 'Post'
    template_name = 'news/posts.html'

class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
