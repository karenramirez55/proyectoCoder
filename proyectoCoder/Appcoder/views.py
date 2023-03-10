from django.shortcuts import render
from Appcoder.models import Profesor,FamiliarUno
from django.http import HttpResponse
from django.template import Template, loader
import datetime

# Create your views here.
def profesor(request):
    profesor=Profesor(nombre='RODOLFO',apellido='BARILO',email='rodo@rodo.com',profesion='MAESTRO')
    profesor.save()
    texto=f'Profe: {profesor.nombre} apellido: {profesor.apellido} email: {profesor.email} profesion: {profesor.profesion}'
    return render(request, 'Appcoder/profesores.html')

def familiar(request):
       familiar=FamiliarUno(nombre='CARLA NAZARETH',apellido='TROVATO', edad=30, fecha_de_nac='1989-5-29')
       familiar.save()
       phrase=f'Name: {familiar.nombre} lastname: {familiar.apellido} Age: {familiar.edad}  Birthdate {familiar.fecha_de_nac}'
       return HttpResponse(phrase)

def inicio(request):
    return render(request,'Appcoder/inicio.html')

def profesores(request):
    return render(request,'Appcoder/profesores.html')

def alumnos(request):
    return render(request,'Appcoder/estudiante.html')

def curso(request):
    return render(request,'Appcoder/cursos.html')

def familiares(request):
        familiar1=FamiliarUno(nombre='CARLA NAZARETH',apellido='TROVATO', edad=33, fecha_de_nac=datetime.date(1989,5,29))
        familiar2=FamiliarUno(nombre='KAREN DENISE',apellido='RAMIREZ', edad=30, fecha_de_nac='1993-1-15')
        familiar3=FamiliarUno(nombre='DAIANA DANIELA',apellido='RAMIREZ', edad=35, fecha_de_nac='1989-10-23')
        familiar1.save()
        familiar2.save()
        familiar3.save()

        diccionario={"familiar1":familiar1,"familiar2":familiar2,"familiar3": familiar3}
        plantilla=loader.get_template('template1.html')
        document=plantilla.render(diccionario)
        return HttpResponse(document)







