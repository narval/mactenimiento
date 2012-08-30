from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import *
from hacePing import *

def index(request):
    if request.user.is_authenticated():
        # aqui la base de datos proporciona la lista de maquinas funcionales
        # por sala y se pasa en el contexto
        maquinas = verMaquinas()
        t = loader.get_template('maquinas.html')
        c = Context({
        'estado' : maquinas,
        })
        return HttpResponse(t.render(c))
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    #return HttpResponse("You're looking at maquina")

def detail(request, maquina_id):
    return HttpResponse("You're looking at maquina %s." % maquina_id)

def results(request, maquina_id):
    return HttpResponse("You're looking at the results of maquina %s." % maquina_id)

def vote(request, maquina_id):
    return HttpResponse("You're voting on maquina %s." % maquina_id)

def prendidas(request):
    import json
    return HttpResponse(json.dumps(verEstado()), mimetype = 'application/javascript')
    
