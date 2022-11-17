from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastroPub/', views.cadastroPub, name='cadastroPub'),
    path('criaPub/', views.criaPub, name='criaPub'),
    path('publicacao/<int:id>/', views.publicacao, name='publicacao'),
    path('favoritar/<int:id>/', views.favoritar, name='favoritar'),
    path('buscar/', views.buscar, name='buscar'),
    path('categoria/<int:id>/', views.categoria, name='categoria'),
]
