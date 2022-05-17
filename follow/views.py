from django.shortcuts import render

def follow(request):
    return render(request, 'follow/follow.html')

