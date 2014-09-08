from django.shortcuts import render
from django.forms.models import modelformset_factory
# -*- coding: utf-8 -*-
#import necesarios para trabajar.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from aplicacion.models import Estudiante
from aplicacion.models import Carrera
import json
from django.utils.safestring import mark_safe
#imports para la paginacion
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from models import Turno, Profesional, MyCSvModel
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def manage_turnos(request):
   
    
    TunoFormSet = modelformset_factory(Turno)
    if request.method == 'POST':
        print "si"
        formset = TunoFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return render_to_response("gracias.html")
    else:
        print "no"
        formset = TunoFormSet()
        profesional_list= Profesional.objects.all()
        turno_list= Turno.objects.all()
        
    return render_to_response("prue.html", {
        "formset": formset,"profesional": profesional_list, "turno": turno_list
    })
def importCSV(request):
	my_csv_list = MyCSvModel.import_data(data = open('my_csv_file_name.csv'))
	return render(request, 'index.html')
def index(request):
    profesional_list= Profesional.objects.all()
    turno_list= Turno.objects.all()
    return render_to_response("examples.html", { "profesional": profesional_list, "turno": turno_list },  context_instance=RequestContext(request))

def gracias(request):
    return render(request, 'gracias.html')
def vote(request, p_id):
    p = get_object_or_404(Profesional, pk=p_id)
    try:
        selected_choice = Turno.objects.filter(pk=1)#request.POST['turno']
    except (KeyError, Turno.DoesNotExist):
        return render(request, 'gracias.html')
    else:
       selected_choice.disponible += 1
       selected_choice.save()
       return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    #return render(request, 'gracias.html')
