from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Desde la visa de encuestas!</h1><p>pueva</p>")

def suma(request, n1_id, n2_id):
    n1=n1_id
    n2=n2_id
    res= n1_id +n2_id
    return HttpResponse("La Respuesta de la suma de {n1} + {n2} es igual a {res}".format(n1=n1, n2=n2, res=res)) 

def resta(request, n1_id, n2_id):
    n1=n1_id
    n2=n2_id
    res= n1_id - n2_id
    return HttpResponse("La Respuesta de la resta de {n1} - {n2} es igual a {res}".format(n1=n1, n2=n2, res=res))

def multiplicacion(request, n1_id, n2_id):
    n1=n1_id
    n2=n2_id
    res= n1_id * n2_id
    response = "Estas viendo los resultado de la pregunta %s."
    return HttpResponse("La Respuesta de la multiplicacion de {n1} * {n2} es igual a {res}".format(n1=n1, n2=n2, res=res))

def division(request, n1_id, n2_id):
    n1=n1_id
    n2=n2_id
    res= n1_id / n2_id
    return HttpResponse("La Respuesta de la division de {n1} / {n2} es igual a {res}".format(n1=n1, n2=n2, res=res))

