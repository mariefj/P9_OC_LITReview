from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import forms
from . import models

@login_required
def home(request):
    return render(request, 'feed/home.html')

def posts(request):
    return render(request, 'feed/posts.html')

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

