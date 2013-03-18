# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response

def home(request):
	return HttpResponse("Texto")

def post (request,id):
	return HttpResponse("Este es el post %i" % int(id))

def hora_actual(request):
	ahora = datetime.now()
	return render_to_response('hora.html',{'hora':ahora,'list': range(4)})

def hora_actual2(request):
	ahora = datetime.now()
	t = get_template('hora.html')
	c = Context ({'hora': ahora})
	html = t.render(c)
	return HttpResponse(html)