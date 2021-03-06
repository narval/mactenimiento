from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from views import *

def index(request):
    """
    if request.user.is_authenticated():
        #arequest.session[]
        #return HttpResponse("Hello, world. You're at the maquina index.")
        estado = verEstado()
        t = loader.get_template('maquinas.html')
        c = Context({
            'estado': estado,
        })
        return HttpResponse(t.render(c))
    else:
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    """
    return HttpResponse("pagina principal sapo")

def detail(request, maquina_id):
    return HttpResponse("You're looking at maquina %s." % maquina_id)

def results(request, maquina_id):
    return HttpResponse("You're looking at the results of maquina %s." % maquina_id)

def vote(request, maquina_id):
    return HttpResponse("You're voting on maquina %s." % maquina_id)
