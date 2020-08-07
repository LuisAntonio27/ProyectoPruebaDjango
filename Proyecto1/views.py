from django.http import HttpResponse

def saludo(request): #primera vista
	return HttpResponse("Primera p&aacute;gina con Django")

def despedida(request):
	return HttpResponse("Despedida de Django")