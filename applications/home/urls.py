from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        'home/', 
        views.home.as_view(),
        name='pagina-inicio',
    ),
    ]