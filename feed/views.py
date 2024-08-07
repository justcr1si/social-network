from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PostCreationForm
from .models import Post
from profile_page.models import User


def display_feed(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'feed/feed.html', context)


@login_required(login_url='/profile/login/')
def create_post(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = PostCreationForm(data=request.POST)
        if form.is_valid():
            topic = request.POST.get('topic')
            text = request.POST.get('text')
            if text:
                Post.objects.create(user=user, topic=topic, text=text)
                return redirect('feed')
    else:
        form = PostCreationForm()

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'feed/create_post.html', context)
