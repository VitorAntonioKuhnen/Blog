from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastroPub/', views.cadastroPub, name='cadastroPub'),
    path('criaPub/', views.criaPub, name='criaPub'),
    path('publicacao/<int:id>/', views.publicacao, name='publicacao'),
]