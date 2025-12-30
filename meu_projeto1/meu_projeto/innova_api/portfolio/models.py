from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    gestor = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    TIPO_CHOICES = [
        ('Linguagem', 'Linguagem'),
        ('Framework', 'Framework'),
        ('Servico Cloud', 'Serviço Cloud'),
        ('Banco de Dados', 'Banco de Dados'),
        ('Outro', 'Outro'),
    ]
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    versao = models.CharField(max_length=50, blank=True, null=True)
    fornecedor = models.CharField(max_length=100, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"

class Projeto(models.Model):
    STATUS_CHOICES = [
        ('Planejado', 'Planejado'),
        ('Em Execução', 'Em Execução'),
        ('Concluido', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    ]
    
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='projetos')
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Planejado')
    
   
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')

    def __str__(self):
        return self.nome
