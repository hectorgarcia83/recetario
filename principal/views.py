from principal.models import Receta
from django.shortcuts import render_to_response

def lista_recetas(request):
	recetas = Receta.objects.all()
	return render_to_response('lista_recetas.html',{'lista':recetas})