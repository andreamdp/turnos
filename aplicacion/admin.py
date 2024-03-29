# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Turno, Estudiante, Carrera, Profesional, MyCSvModel


def importCsv(modeladmin, request, queryset):
    my_csv_list = MyCSvModel.import_data(data = open("my_csv_file_name.csv"))




class ProfeAdmin(admin.ModelAdmin):
    actions = [importCsv]  
 
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('Codigo','__unicode__','Nacimiento','Direccion','Email','Telefono','Carrera')
    search_fields = ('Nombres','ApellidoPaterno','ApellidoMaterno',)
    radio_fields = { "Sexo": admin.HORIZONTAL}
    list_filter = ('Carrera',)
admin.site.register(Estudiante, EstudianteAdmin)
 
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('Carrera','Codigo')
    search_fields = ('Carrera','Codigo')
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Turno)
admin.site.register(Profesional, ProfeAdmin)
