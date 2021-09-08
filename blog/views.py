from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, status='published', slug=post_slug)
    return render(request, 'blog/post/detail.html', {'post': post})
