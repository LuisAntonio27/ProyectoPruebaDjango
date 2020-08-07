from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): #primera vista
	doc_externo = open("Proyecto1/plantillas/miplantilla.html")
	plantilla = Template(doc_externo.read())
	doc_externo.close()
	contexto = Context()
	documento = plantilla.render(contexto)
	return HttpResponse(documento)

def despedida(request):
	return HttpResponse("Despedida de Django")

def dameFecha(request):
	fecha_actual = datetime.datetime.now()
	return HttpResponse("Fecha y hora actuales: %s" %fecha_actual)

def calculaEdad(request, edad, year):
	periodo = year - datetime.datetime.now().year
	edadFutura = edad + periodo
	return HttpResponse("En el año %s tendras %s años" %(year, edadFutura))