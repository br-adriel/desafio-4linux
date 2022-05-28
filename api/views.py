from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from salas.models import Sala
from salas.serializers import SalaSerializer


class ListarSalas(ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class SalasDisponiveis(ListAPIView):
    queryset = Sala.objects.filter(disponivel=True)
    serializer_class = SalaSerializer


@api_view(['GET'])
def buscar_salas(request, nome):
    salas = Sala.objects.filter(nome__icontains=nome)
    serializer = SalaSerializer(salas, many=True)
    return Response(serializer.data)
