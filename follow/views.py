from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import User
from . import models
from . import forms

@login_required
def follow(request):
    if request.method == 'GET':
        # form = forms.UserFollowsForm()
        form = forms.UserFollowsForm(user=request.user)
        followed_users = models.UserFollows.objects.filter(user=request.user)
        following_users = models.UserFollows.objects.filter(followed_user=request.user)
        context = {'form': form, 'followed_users': followed_users, 'following_users': following_users}
        return render(request, 'follow/follow.html', context)
    elif request.method == 'POST':
        followed_user = User.objects.get(pk=request.POST["followed_user"])
        models.UserFollows.objects.create(user=request.user, followed_user=followed_user)
        return redirect('home')

@login_required
def unfollow(request, id_user):
    if request.method == 'POST':
        relation = models.UserFollows.objects.get(user=request.user, followed_user=id_user)
        if relation:
            relation.delete()
        return redirect('home')

