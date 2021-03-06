from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):

	def __init__(self, nombre, apellido):
	    self.nombre = nombre
	    self.apellido = apellido

def saludo(request): #primera vista

	p1 = Persona("Profesor antonio", "Cruz")

	nombre = "Luis"
	apellido = "Cruz"
	ahora = datetime.datetime.now()

	temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
	# temasDelCurso = ""

	# mediante esta forma, el template que es creado y al momento de renderizarlo, si acepta el contexto creado despues
	# doc_externo = open("Proyecto1/plantillas/miplantilla.html")
	# plantilla = Template(doc_externo.read())
	# doc_externo.close()
	# contexto = Context({"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "momento_actual" : ahora.strftime("%x"), "temas" : temasDelCurso})
	# documento = plantilla.render(contexto)

	# con un loader, al renderizarlo solo acepta un diccionario y no el contexto creado anteriormente
	# con la clase importada shortcuts ya no necesitamos de los cargadores

	# doc_externo = loader.get_template('miplantilla.html')
	# documento = doc_externo.render({"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "momento_actual" : ahora.strftime("%x"), "temas" : temasDelCurso})
	# return HttpResponse(documento)

	return render(request, "miplantilla.html", {"nombre_persona" : p1.nombre, "apellido_persona" : p1.apellido, "momento_actual" : ahora.strftime("%x"), "temas" : temasDelCurso})

def cursoC(request):
	ahora = datetime.datetime.now()
	return render(request, "cursoC.html", {"dameFecha" : ahora})

def cursoCss(request):
	ahora = datetime.datetime.now()
	return render(request, "cursoCss.html", {"dameFecha" : ahora})

def despedida(request):
	return HttpResponse("Despedida de Django")

def dameFecha(request):
	fecha_actual = datetime.datetime.now()
	return HttpResponse("Fecha y hora actuales: %s" %fecha_actual)

def calculaEdad(request, edad, year):
	periodo = year - datetime.datetime.now().year
	edadFutura = edad + periodo
	return HttpResponse("En el año %s tendras %s años" %(year, edadFutura))