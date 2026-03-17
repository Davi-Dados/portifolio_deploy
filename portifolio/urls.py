from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('listas_projetos/',views.lista_projetos, name="lista_projetos"),
    path('projeto/<str:id_projeto>/',views.detalhes_projetos,name="detalhes_projetos"),
]
