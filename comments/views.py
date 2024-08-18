from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from feed.models import Post
from .models import Comment
from .forms import CommentForm
from profile_page.models import User


def view_comments(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = post.comments.all()

    context = {
        'comments': comments,
        'post': post,
    }

    return render(request, 'comments/view_comments.html', context)


@login_required(login_url='/profile/login/')
def leave_comment(request, post_id, user_id=None):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if user_id:
            user = User.objects.get(pk=user_id)
        text = request.POST.get('text')
        if text:
            Comment.objects.create(user=user, post=post, text=text)
            return redirect('comments:view-comments', post_id=post_id)
    else:
        form = CommentForm()

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'comments/leave_comment.html', context)
