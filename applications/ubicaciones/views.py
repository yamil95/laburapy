from django.shortcuts import render
from django.urls import reverse
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout
from django.http import HttpResponse

from .models import Provincias,Localidades
#https://apis.datos.gob.ar/georef/api/departamentos?provincia=Buenos Aires&max=200
#https://apis.datos.gob.ar/georef/api/provincias

import requests
"""

"""
from django.http import JsonResponse

def get_localidades(request, provincia_id):
    localidades = Localidades.objects.filter(provincia_id=provincia_id)
    data = [{'id': loc.id, 'nombre': loc.nombre} for loc in localidades]
    return JsonResponse(data, safe=False)

def cargar_provincias(request):

    # Realiza la consulta a la API externa
    try:

        response = requests.get('https://apis.datos.gob.ar/georef/api/provincias')
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        
        # Procesa los datos de la respuesta
        data = response.json()
        
        # Crea los objetos Ubicaciones y guárdalos en la base de datos
        lista_provincias = []
        for provincia in data["provincias"]:
            provincia_db = Provincias(nombre = provincia["nombre"])
            lista_provincias.append(provincia_db)
        
        Provincias.objects.bulk_create(lista_provincias)
        return HttpResponse('Provincias cargadas exitosamente')
    
    except RequestException as e:
        # Captura cualquier excepción relacionada con la solicitud
        return HttpResponse('Error en la solicitud: {}'.format(str(e)))
    
    except HTTPError as e:
        # Captura errores HTTP
        return HttpResponse('Error HTTP: {}'.format(str(e)))
    
    except ConnectionError as e:
        # Captura errores de conexión
        return HttpResponse('Error de conexión: {}'.format(str(e)))
    
    except Timeout as e:
        # Captura errores de tiempo de espera
        return HttpResponse('Tiempo de espera agotado: {}'.format(str(e)))


    
def cargar_localidades (request):
        

    try:
        nombres_provincias = [provincia.nombre for provincia in Provincias.objects.all()]
        lista_localidades = []
        for provincia in nombres_provincias:
            url = f"https://apis.datos.gob.ar/georef/api/departamentos?provincia={provincia}&max=150"
            response = requests.get(url)
            response.raise_for_status()  # Lanza una excepción si hay un error HTTP
            
            # Procesa los datos de la respuesta
            data = response.json()
            
            # Crea los objetos Ubicaciones y guárdalos en la base de datos
            
            for departamento in data["departamentos"]:
                nombre_provincia = departamento['provincia']['nombre']
                nombre_localidad= departamento["nombre"]
                #print (nombre_provincia,"+",nombre_localidad)
                provincia_db, created = Provincias.objects.get_or_create(nombre=nombre_provincia)
                localidad = Localidades(nombre=nombre_localidad,provincia=provincia_db)
                lista_localidades.append(localidad)
        
        Localidades.objects.bulk_create(lista_localidades)
        return HttpResponse('Localidades cargadas exitosamente')

    except RequestException as e:
        # Captura cualquier excepción relacionada con la solicitud
        return HttpResponse('Error en la solicitud: {}'.format(str(e)))

    except HTTPError as e:
        # Captura errores HTTP
        return HttpResponse('Error HTTP: {}'.format(str(e)))

    except ConnectionError as e:
        # Captura errores de conexión
        return HttpResponse('Error de conexión: {}'.format(str(e)))

    except Timeout as e:
        # Captura errores de tiempo de espera
        return HttpResponse('Tiempo de espera agotado: {}'.format(str(e)))

    
    

