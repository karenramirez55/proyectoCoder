from django.db import models

class Curso(models.Model):
    nombres=models.CharField(max_length=40)
    comision=models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)

class Entregable(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_de_entrega=models.DateField()
    entregable=models.BooleanField()

class FamiliarUno(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    fecha_de_nac=models.DateField()







# Create your models here.
