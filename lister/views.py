from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from lister.models import Info
from lister.models import Client
from lister.models import Type
import ipaddress
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Tableau des clés
class UpdateView(TemplateView):
  template_name = 'update.html'
  def get(self, request, **kwargs):
    info = Info.objects.all()
    client = Client.objects.all()
    type = Type.objects.all()
    return render(request, self.template_name, {'info' : info, 'client': client, 'type' : type})

class AddView(TemplateView):
  template_name = 'add.html'
  def get(self, request, **kwargs):
    info = Info.objects.all()
    client = Client.objects.all()
    type = Type.objects.all()
    return render(request, self.template_name, {'info' : info, 'client': client, 'type' : type})

class PleaseLog(TemplateView):
    def get(self, request, **kwargs):
        messages.error(request, 'Veuillez vous connecter')
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
# Connexion
class LoginView(TemplateView):
  template_name = 'index.html'

  def get(self, request, **kwargs):
    info = Info.objects.all()
    client = Client.objects.all()
    type = Type.objects.all()
    return render(request, self.template_name, {'info' : info, 'client': client, 'type' : type})

class DeleteInfo(TemplateView):
  template_name = 'index.html'
  def post(self, request, **kwargs):
    infoid = request.POST.get('info_id', False)
    Info.objects.filter(id=infoid).delete()
    messages.success(request, "L'info a bien été supprimée")
    return HttpResponseRedirect( "/update/" )

class UpdateInfo(TemplateView):
  template_name = 'index.html'
  def post(self, request, **kwargs):
    ip = request.POST.get('ip', False)  
    try:
      ipaddress.ip_address(ip)
    except:
      messages.error(request, 'Mauvais format IP')
      return HttpResponseRedirect( "/update/" )
    url = request.POST.get('url', False)
    try:
      URLValidator()(url)
    except:
      messages.error(request, 'Mauvaise URL')
      return HttpResponseRedirect( "/update/" )    
    clientnom = request.POST.get('client', False)
    hostname = request.POST.get('hostname', False)
    typenom = request.POST.get('type', False)
    try:
      clientid = Client.objects.get(nom=clientnom).id
      typeid = Type.objects.get(nom=typenom).id
    except:
      messages.error(request, 'Mauvais client ou type')
      return HttpResponseRedirect( "/update/" )
    formid = request.POST.get('formid', False)
    try:
      Info.objects.filter(id=formid).update(url=url, ip=ip, cli_id=clientid, typ_id = typeid, hostname=hostname)
      messages.success(request, "L'info a bien été modifiée")
      return HttpResponseRedirect( "/update/" )
    except:
      messages.error(request, "Impossible de mettre a jour l'info")
      return HttpResponseRedirect( "/update/" )

class AjouterType(TemplateView):
  template_name = "index.html"
  def post(self, request, **kwargs):
    typenom = request.POST.get('type', False)
    try:
      t = Type(nom=typenom)
      t.save()
      messages.success(request, 'Le type a bien été ajouté')
      return HttpResponseRedirect( "/add/" )
    except:
      messages.error(request, "Impossible de créer un type")
      return HttpResponseRedirect( "/add/" )

class AjouterClient(TemplateView):
  template_name = "index.html"
  def post(self, request, **kwargs):
    clientnom = request.POST.get('client', False)
    try:
      c = Client(nom=clientnom)
      c.save()
      messages.success(request, 'Le client a bien été ajouté')
      return HttpResponseRedirect( "/add/" )
    except:
      messages.error(request, "Impossible de créer un client")
      return HttpResponseRedirect( "/add/" )

class AjouterInfo(TemplateView):
  template_name = "index.html"
  def post(self, request, **kwargs):
    ip = request.POST.get('ip', False)  
    try:
      ipaddress.ip_address(ip)
    except:
      messages.error(request, 'Mauvais format IP')
      return HttpResponseRedirect( "/add/" )
    url = request.POST.get('url', False)
    try:
      URLValidator()(url)
    except:
      messages.error(request, 'Mauvaise URL')
      return HttpResponseRedirect( "/add/" )    
    clientnom = request.POST.get('client', False)
    hostname = request.POST.get('hostname', False)
    typenom = request.POST.get('type', False)
    try:
      clientid = Client.objects.get(nom=clientnom).id
      typeid = Type.objects.get(nom=typenom).id
    except:
      messages.error(request, "Mauvais client ou type")
      return HttpResponseRedirect( "/add/" )
    try:
      i = Info(ip=ip, hostname=hostname, url=url, cli_id = clientid, typ_id = typeid)
      i.save()
      messages.success(request, "L'info a bien été ajoutée")
      return HttpResponseRedirect( "/add/" )
    except:
      messages.error(request, "Impossible de créer une info")
      return HttpResponseRedirect( "/add/" )
