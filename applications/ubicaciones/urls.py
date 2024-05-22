#
from django.urls import path

from . import views

app_name = "ubicaciones_app"

urlpatterns = [
    path(
       'cargar-provincias/', 
        views.cargar_provincias,
        name='cargar-provincias',
    ),
    path(
       'cargar-localidades/', 
        views.cargar_localidades,
        name='cargar-localidades',
    ),
    path(
        'get-localidades/<int:provincia_id>/',
         views.get_localidades, 
         name='get-localidades')

]