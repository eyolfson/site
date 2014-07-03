# Copyright 2014 Jon Eyolfson
#
# This file is distributed under the GPLv3 license

from django.shortcuts import get_object_or_404, render

from django_blog.models import Post

def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/index.html', context)

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post})
