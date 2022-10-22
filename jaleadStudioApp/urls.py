from django.urls import path

from . import views # Importar views.py

urlpatterns = [
    path('', views.inicio, name='inicio'),
]