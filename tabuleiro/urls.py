from django.urls import path
from . import views

urlpatterns = [
    path('', views.tabuleiro_view, name='tabuleiro'),
    path('iniciar-busca/', views.iniciar_busca, name='iniciar_busca'),
    path('proxima-solucao/', views.proxima_solucao, name='proxima_solucao'),
]
