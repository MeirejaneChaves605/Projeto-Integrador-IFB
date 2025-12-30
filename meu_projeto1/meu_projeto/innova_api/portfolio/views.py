from rest_framework import viewsets
from .models import Departamento, Projeto, Tecnologia
from .serializers import DepartamentoSerializer, ProjetoSerializer, TecnologiaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['ativo']
    search_fields = ['nome', 'gestor']

class TecnologiaViewSet(viewsets.ModelViewSet):
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['tipo', 'fornecedor']
    search_fields = ['nome', 'descricao']


class ProjetoViewSet(viewsets.ModelViewSet):
    
    queryset = Projeto.objects.all().select_related('departamento').prefetch_related('tecnologias') 
    serializer_class = ProjetoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    
    filterset_fields = [
        'departamento', 
        'status', 
        'tecnologias', 
        'data_inicio',
        'data_fim'
    ]
    
   
    filter_fields = {
        'data_inicio': ['exact', 'gte', 'lte'],
        'data_fim': ['exact', 'gte', 'lte'],
    }
    
    search_fields = ['nome', 'descricao']
    ordering_fields = ['data_inicio', 'status']

    def departamentos_view(request):
   
        return render(request, 'departamentos.html') 

    def tecnologias_view(request):
        return render(request, 'tecnologias.html')

