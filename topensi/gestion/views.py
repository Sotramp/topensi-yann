from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
import ipaddress

# Create your views here.
class IndexView(TemplateView):
  template_name = 'index.html'
  def get(self, request, **kwargs):
    return render(request, self.template_name)

class AddView(TemplateView):
  template_name = 'add.html'
  def get(self, request, **kwargs):
    return render(request, self.template_name)