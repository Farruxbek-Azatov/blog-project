from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, status='published', id=post_id)
    return render(request, 'blog/post/detail.html', {'post': post})
