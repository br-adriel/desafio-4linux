from rest_framework.generics import ListCreateAPIView, ListAPIView
from salas.models import Sala
from salas.serializers import SalaSerializer


class ListarSalas(ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class SalasDisponiveis(ListAPIView):
    queryset = Sala.objects.filter(disponivel=True)
    serializer_class = SalaSerializer
