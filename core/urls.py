from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastro_aluno/', views.cadastro_aluno, name="cadastro-aluno"),
    path('presenca/', views.presenca, name="presenca"),
    path('teladiretor/', views.tela_diretor, name="tela-diretor"),
    path('turno/', views.turno, name="turno"),
    path('tela-cadastro/', views.tela_cadastro, name="tela-cadastro"),
   
]
