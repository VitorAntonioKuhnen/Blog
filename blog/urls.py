from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastroPub/', views.cadastroPub, name='cadastroPub'),
    path('publicacao/', views.publicacao, name='publicacao'),
]