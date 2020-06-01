from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from gestion.models import Info
from gestion.models import Etat
from gestion.models import Client
from gestion.models import Partenaire
from gestion.models import Type
import ipaddress
from django.http import JsonResponse
import month
from django.core import serializers
import datetime
import csv
from urllib.parse import urlparse  # Python 3 

# Create your views here.
class IndexView(TemplateView):
  template_name = 'index.html'
  def get(self, request, **kwargs):
    info = Info.objects.all()
    client = Client.objects.all()
    partenaire = Partenaire.objects.all()
    etat = Etat.objects.all()
    type = Type.objects.all()
    return render(request, self.template_name, {'info' : info, 'client': client, 'partenaire': partenaire, 'type' : type, 'etat': etat})

class AddView(TemplateView):
  template_name = 'add.html'
  def get(self, request, **kwargs):
    info = Info.objects.all()
    client = Client.objects.all()
    partenaire = Partenaire.objects.all()
    etat = Etat.objects.all()
    type = Type.objects.all()
    return render(request, self.template_name, {'info' : info, 'client': client, 'partenaire': partenaire, 'type' : type, 'etat': etat})

class UpdateView(TemplateView):
  template_name = 'update.html'
  def get(self, request, **kwargs):
    info = Info.objects.all()
    client = Client.objects.all()
    partenaire = Partenaire.objects.all()
    etat = Etat.objects.all()
    type = Type.objects.all()
    return render(request, self.template_name, {'info' : info, 'client': client, 'partenaire': partenaire, 'type' : type, 'etat': etat})

class RecurrentView(TemplateView):
  template_name = 'recurrent.html'
  def get(self, request, **kwargs):
    info = Info.objects.all()
    client = Client.objects.all()
    partenaire = Partenaire.objects.all()
    etat = Etat.objects.all()
    type = Type.objects.all()
    return render(request, self.template_name, {'info' : info, 'client': client, 'partenaire': partenaire, 'type' : type, 'etat': etat})

class AddView(TemplateView):
  template_name = 'add.html'
  def get(self, request, **kwargs):
    info = Info.objects.all()
    client = Client.objects.all()
    partenaire = Partenaire.objects.all()
    etat = Etat.objects.all()
    type = Type.objects.all()
    return render(request, self.template_name, {'info' : info, 'client': client, 'partenaire': partenaire, 'type' : type, 'etat': etat})

class UpdateView(TemplateView):
  template_name = 'update.html'
  def get(self, request, **kwargs):
    info = Info.objects.all()
    client = Client.objects.all()
    partenaire = Partenaire.objects.all()
    etat = Etat.objects.all()
    type = Type.objects.all()
    return render(request, self.template_name, {'info' : info, 'client': client, 'partenaire': partenaire, 'type' : type, 'etat': etat})

class AjouterPartenaireView(TemplateView):
  template_name = "index.html"
  def post(self, request, **kwargs):
    partenaire = request.POST.get('partenaire', False)
    try:
      p = Partenaire(nom=partenaire)
      p.save()
      messages.success(request, 'Le partenaire a bien été ajouté')
      return HttpResponseRedirect( "/add/" )
    except:
      messages.error(request, "Impossible de créer un partenaire")
      return HttpResponseRedirect( "/add/" )

class AjouterClientView(TemplateView):
  template_name = "index.html"
  def post(self, request, **kwargs):
    client = request.POST.get('client', False)
    try:
      c = Client(nom=client)
      c.save()
      messages.success(request, 'Le client a bien été ajouté')
      return HttpResponseRedirect( "/add/" )
    except:
      messages.error(request, "Impossible de créer un client")
      return HttpResponseRedirect( "/add/" )

class AjouterTypeView(TemplateView):
  template_name = "index.html"
  def post(self, request, **kwargs):
    type = request.POST.get('type', False)
    try:
      c = Type(nom=type)
      c.save()
      messages.success(request, 'Le type a bien été ajouté')
      return HttpResponseRedirect( "/add/" )
    except:
      messages.error(request, "Impossible de créer un type")
      return HttpResponseRedirect( "/add/" )

class AjouterEtatView(TemplateView):
  template_name = "index.html"
  def post(self, request, **kwargs):
    type = request.POST.get('etat', False)
    try:
      c = Etat(nom=type)
      c.save()
      messages.success(request, 'Le etat a bien été ajouté')
      return HttpResponseRedirect( "/add/" )
    except:
      messages.error(request, "Impossible d'ajouter l'état")
      return HttpResponseRedirect( "/update/")

class AjouterInfoView(TemplateView):
  template_name = "index.html"
  def post(self, request, **kwargs):
    client = request.POST.get('client', False)
    partenaire = request.POST.get('partenaire', False) 
    type = request.POST.get('type', False)
    etat = request.POST.get('etat', False)
    try:
      type_id = Type.objects.get(nom=type)
      etat_id = Etat.objects.get(nom=etat)
      partenaire_id = Partenaire.objects.get(nom=partenaire)
      client_id = Client.objects.get(nom=client)
    except:
      messages.error(request, "Veuillez remplir tous les champs!")
      return HttpResponseRedirect( "/add/" )
    marge = request.POST.get('marge', False)
    recurrent = request.POST.get('recurrent', False)
    facture = request.POST.get('facture', False)
    dateCreation = request.POST.get('dateCreation', False)
    dateCloture = request.POST.get('dateCloture', False)
    try:
      if(dateCloture == ''):
        dateCloture = "1970-01"
      i = Info(cli=client_id, partenaire=partenaire_id, typ=type_id, etat=etat_id,marge=marge, recurrent=recurrent, facture=facture, dateCloture = dateCloture, dateCreation = dateCreation)
      i.save()
      messages.success(request, "L'info a bien été ajoutée")
      return HttpResponseRedirect( "/add/" )
    except:
      messages.error(request, "Impossible d'ajouter l'info")
      return HttpResponseRedirect( "/add/" )

class FilterInfoView(TemplateView):
  template_name = "index.html"
  def post(self, request, **kwargs):
    etat = request.POST.get('etat', False)
    partenaire = request.POST.get('partenaire', False)
    type = request.POST.get('type', False)
    dcreation = request.POST.get('dcreation', False)
    fcreation = request.POST.get('fcreation', False)
    dcloture = request.POST.get('dcloture', False)
    fcloture = request.POST.get('fcloture', False)
    client = request.POST.get('client', False)
    try:
      to_send = Info.objects.all()
    except:
      messages.error(request, "Impossible de récupérer les infos")
      return HttpResponseRedirect( "/update/")
    exclude = []
    if fcreation != '':
      for e in to_send:
        if e.dateCreation > fcreation:
          exclude.append(e.id)
    if dcreation != '':
      for e in to_send:
        if e.dateCreation < dcreation:
          exclude.append(e.id)
    if fcloture != '':
      for e in to_send:
        if e.dateCloture > fcloture:
          exclude.append(e.id)
        elif e.dateCloture == '1970-01':
          exclude.append(e.id)
    if dcloture != '':
      for e in to_send:
        if e.dateCloture < dcloture:
          exclude.append(e.id)
        elif e.dateCloture == '1970-01':
          exclude.append(e.id)
    to_send = to_send.exclude(id__in=exclude)
    if etat != 'False':
      to_send = to_send.filter(etat_id=etat)
    if partenaire != 'False':
      to_send = to_send.filter(partenaire_id=partenaire)
    if type != 'False':
      to_send = to_send.filter(typ_id=type)
    if client != 'False':
      to_send = to_send.filter(cli_id=client)
    leads_as_json = serializers.serialize('json', to_send)
    return HttpResponse(leads_as_json, content_type='json')

class DeleteInfo(TemplateView):
  template_name = 'update.html'
  def post(self, request, **kwargs):
    infoid = request.POST.get('info_id', False)
    try:
      Info.objects.filter(id=infoid).delete()
      messages.success(request, "L'info a bien été supprimée")
      return HttpResponseRedirect( "/update/" )
    except:
      messages.error(request, "Impossible de supprimer l'info")
      return HttpResponseRedirect( "/update/")

class UpdateInfo(TemplateView):
  template_name = 'update.html'
  def post(self, request, **kwargs):
    recurrent = request.POST.get('recurrent', False)  
    marge = request.POST.get('marge', False)
    facture = request.POST.get('facture', False)
    dateCloture = request.POST.get('datecloture', False)
    dateCreation = request.POST.get('datecreation', False)  
    clientnom = request.POST.get('client', False)
    partenairenom = request.POST.get('partenaire', False)
    typenom = request.POST.get('type', False)
    etatnom = request.POST.get('etat', False)
    if(dateCloture == ''):
      dateCloture = '1970-01'
    try:
      clientid = Client.objects.get(nom=clientnom).id
      partenaireid = Partenaire.objects.get(nom=partenairenom).id
      typeid = Type.objects.get(nom=typenom).id
      etatid = Etat.objects.get(nom=etatnom).id
    except:
      messages.error(request, "Impossible de récupérer l'info")
      return HttpResponseRedirect( "/update/")
    formid = request.POST.get('formid', False)
    try:
      Info.objects.filter(id=formid).update(recurrent=recurrent, facture=facture, marge=marge, dateCloture=dateCloture, dateCreation=dateCreation, cli_id=clientid, typ_id = typeid, partenaire_id=partenaireid, etat_id=etatid) 
      messages.success(request, "L'info a bien été modifiée")
      return HttpResponseRedirect( "/update/" )
    except:
      messages.error(request, "Impossible de mettre a jour l'info")
      return HttpResponseRedirect( "/update/" )

class UpdateRecurrent(TemplateView):
  template_name = 'recurrent.html'
  def post(self, request, **kwargs):
    dateInstallation = request.POST.get('dateinstallation', False)
    formid = request.POST.get('formid', False)
    try:
      Info.objects.filter(id=formid).update(dateInstallation=dateInstallation) 
      messages.success(request, "L'info a bien été modifiée")
      return HttpResponseRedirect( "/recurrent/" )
    except:
      messages.error(request, "Impossible de mettre a jour l'info")
      return HttpResponseRedirect( "/recurrent/" )

class FilterRecurrentView(TemplateView):
  template_name = "index.html"
  def post(self, request, **kwargs):
    dinstall = request.POST.get('dinstall', False)
    finstall = request.POST.get('finstall', False)
    dcloture = request.POST.get('dcloture', False)
    fcloture = request.POST.get('fcloture', False)
    try:
      to_send = Info.objects.all()
    except:
      messages.error(request, "Impossible de récupérer les infos")
      return HttpResponseRedirect( "/update/")
    exclude = []
    if finstall != '':
      for e in to_send:
        if e.dateInstallation == None or e.dateInstallation > datetime.datetime.strptime(finstall, '%Y-%m-%d').date():
          exclude.append(e.id)
    if dinstall != '':
      for e in to_send:
        if e.dateInstallation == None or e.dateInstallation < datetime.datetime.strptime(dinstall, '%Y-%m-%d').date():
          exclude.append(e.id)
    if fcloture != '':
      for e in to_send:
        if e.dateCloture > fcloture:
          exclude.append(e.id)
        elif e.dateCloture == '1970-01':
          exclude.append(e.id)
    if dcloture != '':
      for e in to_send:
        if e.dateCloture < dcloture:
          exclude.append(e.id)
        elif e.dateCloture == '1970-01':
          exclude.append(e.id)
    to_send = to_send.exclude(id__in=exclude)
    leads_as_json = serializers.serialize('json', to_send)
    print(leads_as_json)
    return HttpResponse(leads_as_json, content_type='json')

class ExportView(TemplateView):
  template_name = "index.html"
  def get(self, request, **kwargs):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bilan.csv"'
    writer = csv.writer(response)
    print(urlparse(request.META.get('HTTP_REFERER')).path)
    if urlparse(request.META.get('HTTP_REFERER')).path != '/recurrent/':
      writer.writerow(['Client', 'Partenaire', 'Type', 'Marge', 'Recurrent','Etat','Facturé','Date de création','Date de cloture'])
      infos = Info.objects.all().values_list('cli__nom', 'partenaire__nom', 'typ__nom', 'marge', 'recurrent', 'etat','facture','dateCreation','dateCloture')
      for info in infos:
        writer.writerow(info)    
      return response
    else:
      writer.writerow(['Client', 'Partenaire', 'Type', 'Recurrent','Date de cloture','Date d\'installation'])
      infos = Info.objects.all().values_list('cli__nom', 'partenaire__nom', 'typ__nom', 'recurrent', 'dateCloture', 'dateInstallation')
      for info in infos:
        writer.writerow(info)    
      return response
