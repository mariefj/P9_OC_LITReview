"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views
import feed.views
import follow.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('', feed.views.home, name='home'),
    path('posts/', feed.views.posts, name='posts'),
    path('follow/', follow.views.follow, name='follow'),
    path('review/create/', feed.views.review_create, name='review_create'),
    path('ticket/create/', feed.views.ticket_create, name='ticket_create'),
]
