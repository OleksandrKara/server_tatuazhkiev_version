# -*- coding: utf-8 -*-
#from django.http import HttpResponse
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
from django.template import RequestContext
from fotos.models import Foto
#from django.core.mail import send_mail
#from django.http import HttpResponseRedirect

def home_handler(request):
    return render_to_response('home.html')

def main_page(request):
    return render_to_response('index.html')

def ceni_handler(request):
    return render_to_response('ceni.html')
	
def otzivi_handler(request):
    return render_to_response('otzivi.html')

def faq_handler(request):
    return render_to_response('faq.html')

def photo_handler(request):
    fotosGl = Foto.objects.filter(type="Gl")
    fotosGu = Foto.objects.filter(type="Gu")
    fotosBr = Foto.objects.filter(type="Br")
    return render_to_response(template_name='flatpages/photo.html',
	                          dictionary={'fotosGl' : fotosGl, 'fotosGu': fotosGu, 'fotosBr': fotosBr},
							  context_instance=RequestContext(request))