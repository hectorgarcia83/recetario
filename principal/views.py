from principal.models import Receta, Comentario
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def inicio(request):
	recetas = Receta.objects.all()
	return render_to_response('inicio.html',{'recetas':recetas})

def sobre(request):
	html = "<html><body>Proyecto de ejemplo </body></html>"
	return HttpResponse(html)