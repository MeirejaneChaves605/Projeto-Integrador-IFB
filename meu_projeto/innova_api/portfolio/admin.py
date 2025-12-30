from django.contrib import admin
from .models import Departamento, Tecnologia, Projeto


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'gestor', 'ativo', 'data_criacao')
    
    list_filter = ('ativo',)

    search_fields = ('nome', 'gestor', 'descricao')

    fields = ('nome', 'gestor', 'descricao', 'ativo')


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'versao', 'fornecedor')
    list_filter = ('tipo', 'fornecedor')
    search_fields = ('nome', 'descricao')


class TecnologiasInline(admin.TabularInline):
    model = Projeto.tecnologias.through
    extra = 1 

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'departamento', 'status', 'risco', 'orcamento', 'data_inicio', 'data_criacao', 

'listar_tecnologias')
    
    list_filter = ('status', 'departamento', 'tecnologias', 'risco')
    
    search_fields = ('nome', 'descricao')
    ordering = ('-data_inicio',)
    
    fields = (
        'nome', 
        'descricao', 
        'departamento', 
        ('data_inicio', 'data_fim'), 
        'status', 
        ('risco', 'orcamento'), 
        'data_criacao' 
    )
    
   
    readonly_fields = ('data_criacao',) 
    
    
    inlines = [TecnologiasInline]
    
    
    exclude = ('tecnologias',)
    
    
    def listar_tecnologias(self, obj):
        return ", ".join([t.nome for t in obj.tecnologias.all()])
    
    listar_tecnologias.short_description = 'Tecnologias'