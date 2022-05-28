from django.urls import path
from .views import AgendarSala, ListarSalas, SalasDisponiveis, buscar_salas


urlpatterns = [
  path('salas', ListarSalas.as_view(), name='salas'),
  path('salas/disponivel', SalasDisponiveis.as_view(), name='salas-disponiveis'),
  path('salas/buscar/<str:nome>', buscar_salas, name='buscar-salas'),
  path('salas/agendar', AgendarSala.as_view(), name='agendar-sala')
]
