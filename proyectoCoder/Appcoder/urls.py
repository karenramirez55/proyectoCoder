# Si tenemos muchas Aplicaciones APPs sera confuso tener muchos paths en una
# unica urls.py entonces en cada app crearemos nuestras propia URLS.PY
# 1- creamos la urls.py
# 2- import  from django.urls import path
# 3- import las views que ya estaba usando y tenia importadas en mi url anterior
# 4- copiamos y pegamos el urlspatterns que teniamos pero sin el admin y en el otro solo dejamos el admin
# 5- IMPORTANTE relacionamos el urls.py de la app con el proyecto:
#  en la urls de NUESTRO PROYECTO no en la app, aparte de path import include para hacer dicha conexion
#   

from django.urls import path
from Appcoder.views import profesor, familiares , familiar, inicio, profesores, alumnos, curso

urlpatterns = [
    path('profe',profesor),
    path('family',familiar),
    path('familiares',familiares),
    path('profesores',profesores),
    path('alumno',alumnos),
    path('curso',curso),
    path('inicio',inicio),
]
