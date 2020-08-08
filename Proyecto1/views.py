from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

	def __init__(self, nombre, apellido):
	    self.nombre = nombre
	    self.apellido = apellido

def saludo(request): #primera vista

	p1 = Persona("Antonio", "Cruz")

	nombre = "Luis"
	apellido = "Cruz"
	ahora = datetime.datetime.now()

	doc_externo = open("Proyecto1/plantillas/miplantilla.html")
	plantilla = Template(doc_externo.read())
	doc_externo.close()
	contexto = Context({"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido,
		"momento_actual" : ahora})
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