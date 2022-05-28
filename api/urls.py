from django.urls import path
from .views import ListarSalas, SalasDisponiveis


urlpatterns = [
  path('salas', ListarSalas.as_view(), name='salas'),
  path('salas/disponivel', SalasDisponiveis.as_view(), name='salas-disponiveis'),
]
