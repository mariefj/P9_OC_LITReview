from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from itertools import chain

from follow.models import UserFollows

from . import forms
from . import models
from follow.models import UserFollows

@login_required
def home(request):
    followed_users = UserFollows.objects.filter(user=request.user)
    followed = []
    for user in followed_users:
        followed.append(user.followed_user)
    
    tickets = models.Ticket.objects.filter(Q(user=request.user) | Q(user__in=followed))
    reviews = models.Review.objects.filter(Q(user=request.user) | Q(user__in=followed))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'feed/home.html', context={
        'posts': posts,
    })

@login_required
def posts(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'feed/posts.html', context={
        'posts': posts,
    })


@login_required
def ticket_create(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'feed/ticket_create.html', context={'form': form})

@login_required
def review_create(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
   
    return render(request, 'feed/review_create.html', context={
        'ticket_form': ticket_form,
        'review_form': review_form,
    })

@login_required
def ticket_update(request, id_ticket):
    ticket = models.Ticket.objects.get(id=id_ticket)
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()
            return redirect('posts')
    else:
        form = forms.TicketForm(instance=ticket)
    return render(request, 'feed/ticket_update.html', context={'form': form})

@login_required
def review_update(request, id_review):
    review = models.Review.objects.get(id=id_review)
    ticket = review.ticket
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('posts')
    else:
        form = forms.ReviewForm(instance=review)
    return render(request, 'feed/review_update.html', context={'form': form, 'ticket': ticket})

@login_required
def review_answer(request, id_ticket):
    ticket = models.Ticket.objects.get(id=id_ticket)
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    return render(request, 'feed/review_answer.html', context={'form': form, 'ticket': ticket})

@login_required
def ticket_delete(request, id_ticket):
    ticket = models.Ticket.objects.get(id=id_ticket)
    if request.method == 'POST':
        ticket.delete()
        return redirect('posts')
    return render(request, 'feed/post_delete.html', {'ticket': ticket})

@login_required
def review_delete(request, id_review):
    review = models.Review.objects.get(id=id_review)
    if request.method == 'POST':
        review.delete()
        return redirect('posts')
    return render(request, 'feed/post_delete.html', {'review': review})