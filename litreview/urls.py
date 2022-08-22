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
from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import feed.views
import follow.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", authentication.views.login_page, name="login"),
    path("logout/", authentication.views.logout_user, name="logout"),
    path("signup/", authentication.views.signup_page, name="signup"),
    path("", feed.views.home, name="home"),
    path("posts/", feed.views.posts, name="posts"),
    path("follow/", follow.views.follow, name="follow"),
    path("unfollow/<id_user>", follow.views.unfollow, name="unfollow"),
    path("ticket/create/", feed.views.ticket_create, name="ticket_create"),
    path("ticket/<id_ticket>/update", feed.views.ticket_update, name="ticket_update"),
    path("ticket/<id_ticket>/delete", feed.views.ticket_delete, name="ticket_delete"),
    path("review/create/", feed.views.review_create, name="review_create"),
    path("review/<id_ticket>/answer", feed.views.review_answer, name="review_answer"),
    path("review/<id_review>/update", feed.views.review_update, name="review_update"),
    path("review/<id_review>/delete", feed.views.review_delete, name="review_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
