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
    url(r'^recurrent/$', RecurrentView.as_view()),
    url(r'^add/ajouter_client/$', AjouterClientView.as_view()),
    url(r'^add/ajouter_type/$', AjouterTypeView.as_view()),
    url(r'^add/ajouter_partenaire/$', AjouterPartenaireView.as_view()),
    url(r'^add/ajouter_etat/$', AjouterEtatView.as_view()),
    url(r'^add/ajouter_info/$', AjouterInfoView.as_view()),
    url(r'^filter/$', FilterInfoView.as_view()),
    url(r'^filter/recurrent/$', FilterRecurrentView.as_view()),
    url(r'^update/delete/$', DeleteInfo.as_view()),
    url(r'^update/maj/$', UpdateInfo.as_view()),
    url(r'^recurrent/maj/$', UpdateRecurrent.as_view()),
]