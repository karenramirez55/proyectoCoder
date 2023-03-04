from django.shortcuts import render
from Appcoder.models import Profesor,FamiliarUno
from django.http import HttpResponse

# Create your views here.
def profesor(request):
    profesor=Profesor(nombre='RODOLFO',apellido='BARILO',email='rodo@rodo.com',profesion='MAESTRO')
    profesor.save()
    texto=f'Profe: {profesor.nombre} apellido: {profesor.apellido} email: {profesor.email} profesion: {profesor.profesion}'
    return HttpResponse(texto)

def familiar(request):
    familiar=FamiliarUno(nombre='CARLA NAZARETH',apellido='TROVATO', edad=30, fecha_de_nac='1989-5-29')
    familiar.save()
    phrase=f'Name: {familiar.nombre} lastname: {familiar.apellido} Age: {familiar.edad}  Birthdate {familiar.fecha_de_nac}'
    return HttpResponse(phrase)
