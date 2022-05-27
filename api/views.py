from rest_framework.generics import ListAPIView
from salas.models import Sala
from salas.serializers import SalaSerializer


class ListarSalas(ListAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
