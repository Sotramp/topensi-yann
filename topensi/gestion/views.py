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
    print(type)
    c = Etat(nom=type)
    c.save()
    messages.success(request, 'Le etat a bien été ajouté')
    return HttpResponseRedirect( "/add/" )

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
      i = Info(cli=client_id, partenaire=partenaire_id, typ=type_id, etat=etat_id,marge=marge, recurrent=recurrent, facture=facture, dateCloture = dateCloture, dateCreation = dateCreation)
      i.save()
      messages.success(request, "L'info a bien été ajoutée")
      return HttpResponseRedirect( "/add/" )
    except:
      messages.error(request, "Impossible d'ajouter l'info")
      return HttpResponseRedirect( "/add/" )

class DeleteInfo(TemplateView):
  template_name = 'update.html'
  def post(self, request, **kwargs):
    infoid = request.POST.get('info_id', False)
    Info.objects.filter(id=infoid).delete()
    messages.success(request, "L'info a bien été supprimée")
    return HttpResponseRedirect( "/update/" )

class UpdateInfo(TemplateView):
  template_name = 'update.html'
  def post(self, request, **kwargs):
    recurrent = request.POST.get('recurrent', False)  
    marge = request.POST.get('marge', False)
    facture = request.POST.get('facture', False)
    #dateCloture = request.POST.get('datecloture', False)
    #dateCreation = request.POST.get('datecreation', False)  
    clientnom = request.POST.get('client', False)
    partenairenom = request.POST.get('partenaire', False)
    typenom = request.POST.get('type', False)
    etatnom = request.POST.get('etat', False)
    clientid = Client.objects.get(nom=clientnom).id
    partenaireid = Partenaire.objects.get(nom=partenairenom).id
    typeid = Type.objects.get(nom=typenom).id
    etatid = Etat.objects.get(nom=etatnom).id
    #except:
    #messages.error(request, 'Mauvaise saisie')
    #return HttpResponseRedirect( "/update/" )
    formid = request.POST.get('formid', False)
    #try:
    Info.objects.filter(id=formid).update(recurrent=recurrent, facture=facture, marge=marge, dateCloture=dateCloture, dateCreation=dateCreation, cli_id=clientid, typ_id = typeid, partenaire_id=partenaireid, etat_id=etatid) 
    messages.success(request, "L'info a bien été modifiée")
    return HttpResponseRedirect( "/update/" )
    #except:
      #messages.error(request, "Impossible de mettre a jour l'info")
      #return HttpResponseRedirect( "/update/" )
