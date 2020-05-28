from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from gestion.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^add/$', AddView.as_view()),
    url(r'^update/$', UpdateView.as_view()),
]