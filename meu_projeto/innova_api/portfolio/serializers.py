from rest_framework import serializers
from .models import Departamento, Projeto, Tecnologia

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    
    tecnologias = TecnologiaSerializer(many=True, read_only=True) 
    
    tecnologias_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tecnologia.objects.all(),
        many=True,
        write_only=True,
        source='tecnologias'
    )
    
    class Meta:
        model = Projeto
        fields = [
            'id', 
            'nome', 
            'descricao', 
            'departamento', 
            'data_inicio', 
            'data_fim', 
            'status', 
            'risco',
            'orcamento',
            'data_criacao',
            'tecnologias', 
            'tecnologias_ids'
        ]
        
        read_only_fields = ['tecnologias', 'data_criacao']

