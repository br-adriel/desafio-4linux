from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from salas.models import Sala, Agendamento
from salas.serializers import AgendamentoSerializer, SalaSerializer
from django.db.models import Q



class ListarSalas(ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class SalasDisponiveis(ListAPIView):
    queryset = Sala.objects.filter(disponivel=True)
    serializer_class = SalaSerializer


class AgendarSala(CreateAPIView):
    serializer_class = AgendamentoSerializer

    def create(self, request, *args, **kwargs):
        sala = get_object_or_404(Sala, id=request.data.get('sala'))

        agendamentos = Agendamento.objects.filter(
            Q(sala=sala.id) & (
                (Q(fim__lte=request.data.get('fim')) & Q(fim__gte=request.data.get('inicio'))) |
                (Q(inicio__lte=request.data.get('fim')) & Q(inicio__gte=request.data.get('inicio')))
            ))

        if agendamentos.count() > 0:
            return Response({"invalido": "a sala ja esta reservada nessa data e horario"}, status=406)

        return super().create(request, *args, **kwargs)



@api_view(['GET'])
def buscar_salas(request, nome):
    salas = Sala.objects.filter(nome__icontains=nome)
    serializer = SalaSerializer(salas, many=True)
    return Response(serializer.data)
