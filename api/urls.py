from django.urls import path
from .views import ListarSalas


urlpatterns = [
  path('salas', ListarSalas.as_view(), name='salas'),
]
