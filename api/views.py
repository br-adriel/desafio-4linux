from rest_framework.generics import ListCreateAPIView
from salas.models import Sala
from salas.serializers import SalaSerializer


class ListarSalas(ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
