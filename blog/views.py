from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from .models import Post
from .forms import CommentForm, PostShareForm


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, status='published',
                             slug=slug,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    form = CommentForm()
    new_comment = None
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    return render(request, 'blog/post/detail.html', {'post': post,
                                                     'form': form,
                                                     'new_comment': new_comment,
                                                     'comments': comments})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = PostShareForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["name"]} recommends you to read "{post.title}"'
            message = f'Read "{post.title}" at {post_url}\n\n'\
                f'{cd["name"]}\'s comments: {cd["comment"]}'
            send_mail(subject, message, cd['email'], [cd['to']])
            sent = True
    else:
        form = PostShareForm()
    return render(request, 'blog/post/share.html',
                  {'post': post, 'form': form, 'sent': sent})
