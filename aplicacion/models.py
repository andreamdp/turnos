# -*- coding: utf-8 -*-
from django.db import models
from csvImporter.model import CsvDbModel
PROFESIONAL_CHOICES = (
                     ('Ferrando', 'Dr. Juan Carlos Ferrando.'),
                     ('Insaurralde', 'Dr. Rubén O. Insaurralde'),
                     ('Sztern', 'Dr. Jorge Sergio Sztern'),
                     ('Rocatti', 'Dr. Carlos H. Rocatti'),
                 )
class MyCSvModel(CsvDbModel):
    nombre = models.CharField(max_length=30)
    

    class Meta:
        dbModel = 'Profesional'
        delimiter = ";"
                         
class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    class Meta:
     verbose_name = "Profesional"
     verbose_name_plural = "Profesionales"

    def __unicode__(self):
        return self.nombre
        

class Turno(models.Model):
    profesional=models.ForeignKey(Profesional)
    #profesional = models.CharField(max_length=1,choices=PROFESIONAL_CHOICES)
    nombre = models.CharField(max_length=30, null= True, blank=True)
    numero = models.CharField(max_length=6, null= True, blank=True)
  #  fecha = models.DateField()
    hora = models. DateTimeField()
    disponible = models.IntegerField(default=0)


from django.db import models
 
GENDER_CHOICES = (
                     ('M', 'Masculino'),
                     ('F', 'Femenino'),
                 )
 
CIVIL_CHOICES = (
                    ('Soltero', 'Soltero'),
                    ('Casado', 'Casado'),
                    ('Viudo', 'Viudo'),
                    ('Divorciado', 'Divorciado'),
                )
 
class Carrera(models.Model):
    Codigo = models.CharField("Código",max_length=20,unique=True)
    Carrera = models.CharField( max_length=50)
    Observaciones = models.TextField(blank=True,null=True)
 
    def __unicode__(self):
        return self.Carrera
 
    class Meta:
        verbose_name = "Carrera Profesional"
        verbose_name_plural = "Carreras Profesionales"
 
class Estudiante(models.Model):
    Codigo = models.CharField("Código",max_length=7,unique=True)
    Nombres = models.CharField("Nombres",max_length=50)
    ApellidoPaterno = models.CharField("Ape. Pat.",max_length=50)
    ApellidoMaterno = models.CharField("Ape. Mat.",max_length=50)
    Nacimiento = models.DateField("Nacimiento",null=True,blank=True)
    Sexo = models.CharField(max_length=1,choices=GENDER_CHOICES)
    Direccion = models.CharField("Dirección",max_length=150,null=True,blank=True)
    Email = models.EmailField("E-mail",null=True,blank=True)
    EstadoCivil = models.CharField("Estado Civil",max_length=20,choices=CIVIL_CHOICES,default='Soltero')
    Telefono = models.CharField("Teléfono",max_length=20,null=True,blank=True)
    Carrera = models.ForeignKey(Carrera)
    Observaciones = models.TextField(blank=True,null=True)
 
    def __unicode__(self):
        return u'%s %s %s' % (self.ApellidoPaterno,self.ApellidoMaterno,self.Nombres)
 
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiante"
