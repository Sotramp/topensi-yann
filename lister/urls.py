from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from lister.views import *

urlpatterns = [
    url(r'^$', LoginView.as_view()),
    url(r'^add/$', AddView.as_view()),
    url(r'^update/$', UpdateView.as_view()),
    url(r'^add/ajouter_type/$', AjouterType.as_view()),
    url(r'^add/ajouter_client/$', AjouterClient.as_view()),
    url(r'^add/ajouter_info/$', AjouterInfo.as_view()),
    url(r'^please_log/$', PleaseLog.as_view()),
    url(r'^update/delete/$', DeleteInfo.as_view()),
    url(r'^update/maj/$', UpdateInfo.as_view()),

]
