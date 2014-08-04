from django.shortcuts import render

# -*- coding: utf-8 -*-
#import necesarios para trabajar.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from aplicacion.models import Estudiante
from aplicacion.models import Carrera
from django.utils import simplejson
from django.utils.safestring import mark_safe
#imports para la paginacion
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from models import Turno, Profesional
def index(request):
    profesional_list= Profesional.objects.all()
    turno_list= Turno.objects.all()
    return render_to_response("examples.html", { "profesional": profesional_list, "turno": turno_list })
    
def jqgrid_estudiante(request):
    if request.user.is_authenticated() and request.user.has_perm('add_estudiante') or request.user.has_perm('change_estudiante') or request.user.has_perm('delete_estudiante'):
        return render_to_response("jqgrid_estudiante.html", { "user": request.user }, context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('../../')
def ver_jqgrid_estudiante(request):
    if request.user.is_authenticated():
        page = request.GET.get('page','')
        limit = request.GET.get('rows', '')
        sidx = request.GET.get('sidx', '')
        sord = request.GET.get('sord', '')
        busqueda = request.GET.get('_search','')
 
        if sord == 'asc':
            sord = '-'
        elif sord == 'desc':
            sord = ''
 
        students = Estudiante.objects.all()
 
        if busqueda == 'true':
            campo = request.GET.get('searchField','')
            operacion = request.GET.get('searchOper','')
            palabra = request.GET.get('searchString','')
 
            if campo == 'Codigo':
                if operacion == "eq":
                    students = students.filter(Codigo__exact = palabra)
                elif operacion == "nq":
                    students = students.exclude(Codigo__exact = palabra)
                elif operacion == "bw":
                    students = students.filter(Codigo__startswith = palabra)
                elif operacion == "bn":
                    students = students.exclude(Codigo__startswith = palabra)
                elif operacion == "ew":
                    students = students.filter(Codigo__endswith = palabra)
                elif operacion == "en":
                    students = students.exclude(Codigo__endswith = palabra)
                elif operacion == "cn":
                    students = students.filter(Codigo__contains = palabra)
                elif operacion == "nc":
                    students = students.exclude(Codigo__contains = palabra)
            elif campo == 'ApellidoPaterno':
                if operacion == "eq":
                    students = students.filter(ApellidoPaterno__exact = palabra)
                elif operacion == "nq":
                    students = students.exclude(ApellidoPaterno__exact = palabra)
                elif operacion == "bw":
                    students = students.filter(ApellidoPaterno__startswith = palabra)
                elif operacion == "bn":
                    students = students.exclude(ApellidoPaterno__startswith = palabra)
                elif operacion == "ew":
                    students = students.filter(ApellidoPaterno__endswith = palabra)
                elif operacion == "en":
                    students = students.exclude(ApellidoPaterno__endswith = palabra)
                elif operacion == "cn":
                    students = students.filter(ApellidoPaterno__contains = palabra)
                elif operacion == "nc":
                    students = students.exclude(ApellidoPaterno__contains = palabra)
            elif campo == 'ApellidoMaterno':
                if operacion == "eq":
                    students = students.filter(ApellidoMaterno__exact = palabra)
                elif operacion == "nq":
                    students = students.exclude(ApellidoMaterno__exact = palabra)
                elif operacion == "bw":
                    students = students.filter(ApellidoMaterno__startswith = palabra)
                elif operacion == "bn":
                    students = students.exclude(ApellidoMaterno__startswith = palabra)
                elif operacion == "ew":
                    students = students.filter(ApellidoMaterno__endswith = palabra)
                elif operacion == "en":
                    students = students.exclude(ApellidoMaterno__endswith = palabra)
                elif operacion == "cn":
                    students = students.filter(ApellidoMaterno__contains = palabra)
                elif operacion == "nc":
                    students = students.exclude(ApellidoMaterno__contains = palabra)
            elif campo == 'Nombres':
                if operacion == "eq":
                    students = students.filter(Nombres__exact = palabra)
                elif operacion == "nq":
                    students = students.exclude(Nombres__exact = palabra)
                elif operacion == "bw":
                    students = students.filter(Nombres__startswith = palabra)
                elif operacion == "bn":
                    students = students.exclude(Nombres__startswith = palabra)
                elif operacion == "ew":
                    students = students.filter(Nombres__endswith = palabra)
                elif operacion == "en":
                    students = students.exclude(Nombres__endswith = palabra)
                elif operacion == "cn":
                    students = students.filter(Nombres__contains = palabra)
                elif operacion == "nc":
                    students = students.exclude(Nombres__contains = palabra)
 
        estudiantes = students.order_by(str(sord) + str(sidx))
 
        n_estudiantes = estudiantes.count()
        paginator = Paginator(estudiantes, int(limit))
 
        try:
            page = request.GET.get('page', '1')
        except ValueError:
            page = 1
 
        try:
            resultados = paginator.page(page)
        except (EmptyPage, InvalidPage):
            resultados = paginator.page(paginator.num_pages)
 
        filas = []
        i = 1
        for r in resultados.object_list:
            fila = {"id" :r.id, "cell" :[i,r.Codigo,r.ApellidoPaterno,r.ApellidoMaterno,r.Nombres,str(r.Nacimiento),r.Sexo,r.Direccion,r.Email,r.Telefono,r.EstadoCivil,r.Carrera.Carrera,r.Observaciones]}
            filas.append(fila)
            i+=1
        results = {"page": page,"total": paginator.num_pages ,"records": n_estudiantes,"rows": filas }
        return HttpResponse(simplejson.dumps(results, indent=4),mimetype='application/json')
    else:
        return HttpResponseRedirect('../../../')
    
    
def master_jqgrid_estudiante(request):
    if request.user.is_authenticated() and request.GET.get('add','') == 'True' or request.GET.get('change','') == 'True' or request.GET.get('delete','') == 'True':
        operacion = request.POST['oper']
        estudiante_id = request.POST['id']
 
        if operacion == "add" or operacion == "edit":
            codigo = request.POST['Codigo']
            ape_pat = request.POST['ApellidoPaterno']
            ape_mat = request.POST['ApellidoMaterno']
            nombres = request.POST['Nombres']
            nac = request.POST['Nacimiento']
            sexo = request.POST['Sexo']
            direccion = request.POST['Direccion']
            email = request.POST['Email']
            civil = request.POST['EstadoCivil']
            tel = request.POST['Telefono']
            carrera_id = request.POST['Carrera']
            obs = request.POST['Observaciones']
 
        if operacion == "add":
            guardar_estudiante = Estudiante(Codigo = codigo, ApellidoPaterno = ape_pat,ApellidoMaterno = ape_mat, Nombres = nombres, Nacimiento = nac,Sexo = sexo,Direccion = direccion,Email = email, EstadoCivil = civil,Telefono = tel, Carrera_id = carrera_id,Observaciones = obs)
            guardar_estudiante.save()
        elif operacion == "edit":
            obj_estudiante = Estudiante.objects.get(id = estudiante_id)
            obj_estudiante.Codigo = codigo
            obj_estudiante.ApellidoPaterno = ape_pat
            obj_estudiante.ApellidoMaterno = ape_mat
            obj_estudiante.Nombres = nombres
            obj_estudiante.Nacimiento = nac
            obj_estudiante.Sexo = sexo
            obj_estudiante.Direccion = direccion
            obj_estudiante.Email = email
            obj_estudiante.EstadoCivil = civil
            obj_estudiante.Telefono = tel
            obj_estudiante.Carrera_id = carrera_id
            obj_estudiante.Observaciones = obs
            obj_estudiante.save()
        elif operacion == "del":
            obj_estudiante = Estudiante.objects.get(id = estudiante_id)
            obj_estudiante.delete()
        return jqgrid_estudiante(request)
    else:
        return HttpResponseRedirect('../../../')
    
    
    
def obtener_carreras(request):
    if request.user.is_authenticated():
        carreras = Carrera.objects.all()
        inicio_select = "<select>"
        opciones = ""
        for c in carreras:
            opcion = "<option value='%s'>%s</option>" % (c.id, c.Carrera)
            opciones += opcion
        fin_select = "</select>"
        select = inicio_select + opciones + fin_select
        return HttpResponse(mark_safe(select))
    else:
        return HttpResponseRedirect('../../../')
