from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.logar, name='logar'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
]