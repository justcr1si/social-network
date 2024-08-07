from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PostProcessingForm
from .models import Post
from profile_page.models import User


def display_feed(request, user_id=None):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    if user_id:
        user = User.objects.get(pk=user_id)
        context['user'] = user
    return render(request, 'feed/feed.html', context)


@login_required(login_url='/profile/login/')
def create_post(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = PostProcessingForm(data=request.POST)
        if form.is_valid():
            topic = request.POST.get('topic')
            text = request.POST.get('text')
            Post.objects.create(user=user, topic=topic, text=text)
            return redirect('feed:feed')
    else:
        form = PostProcessingForm()

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'feed/create_post.html', context)


@login_required(login_url='/profile/login/')
def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)

    if post:
        post.delete()

    return redirect('feed:feed')


@login_required(login_url='/profile/login/')
def edit_post(request, post_id, user_id=None):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = PostProcessingForm(data=request.POST,
                                  initial={'topic': post.topic, 'text': post.text})
        if form.is_valid():
            topic = request.POST.get('topic')
            text = request.POST.get('text')
            post.topic = topic
            post.text = text
            post.save()
            return redirect('feed:feed')
    else:
        form = PostProcessingForm(
            initial={'topic': post.topic, 'text': post.text})

    context = {
        'post': post,
        'form': form,
    }

    if user_id:
        user = User.objects.get(pk=user_id)
        context['user'] = user

    return render(request, 'feed/edit_post.html', context)
