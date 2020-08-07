from django.http import HttpResponse
import datetime

def saludo(request): #primera vista
	return HttpResponse("Primera p&aacute;gina con Django")

def despedida(request):
	return HttpResponse("Despedida de Django")

def dameFecha(request):
	fecha_actual = datetime.datetime.now()
	return HttpResponse("Fecha y hora actuales: %s" %fecha_actual)

def calculaEdad(request, edad, year):
	periodo = year - datetime.datetime.now().year
	edadFutura = edad + periodo
	return HttpResponse("En el año %s tendras %s años" %(year, edadFutura))