from django.template import Context, loader
from django.http import HttpResponse
from models import *

def index(request):
    return HttpResponse("aqui te logueas")
    #return HttpResponse("You're looking at maquina")

