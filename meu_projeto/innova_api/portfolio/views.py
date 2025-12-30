
from rest_framework import viewsets
from .models import Departamento, Tecnologia, Projeto

from .serializers import (
    DepartamentoSerializer, 
    TecnologiaSerializer, 
    ProjetoSerializer
)


class DepartamentoViewSet(viewsets.ModelViewSet):
    
    serializer_class = DepartamentoSerializer

    queryset = Departamento.objects.all()

class TecnologiaViewSet(viewsets.ModelViewSet):
    
    serializer_class = TecnologiaSerializer
    queryset = Tecnologia.objects.all()

class ProjetoViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProjetoSerializer
    
    queryset = Projeto.objects.all().order_by('-data_inicio')