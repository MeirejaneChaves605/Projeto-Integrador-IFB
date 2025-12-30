import csv
from django.core.management.base import BaseCommand
from portfolio.models import Departamento, Tecnologia, Projeto


CSV_DIR = 'portfolio/data/'
CSV_DELIMITER = ','

class Command(BaseCommand):
    help = 'Importa dados de Departamento, Tecnologia e Projeto a partir de arquivos CSV.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('--- Iniciando a importação de dados para InnovaBank ---'))

        self.importar_departamentos()
        self.importar_tecnologias()
        self.importar_projetos()

        self.stdout.write(self.style.SUCCESS('--- Importação de dados concluída com sucesso! ---'))

   
    def importar_departamentos(self):
        filename = CSV_DIR + 'departamentos.csv'
        self.stdout.write(f'Importando Departamentos de {filename}...')
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=CSV_DELIMITER) 
                count = 0
                for row in reader:
                    row_data = {k.strip(): v.strip() if v is not None else '' 
                                for k, v in row.items() if k is not None}
                    
                    if not row_data.get('nome'):
                        continue
                        
                    try:
                        Departamento.objects.get_or_create(
                            nome=row_data['nome'],
                            defaults={
                                'gestor': row_data.get('gestor'),
                                'descricao': row_data.get('descricao'),
                                'ativo': row_data.get('ativo', '').lower() == 'true', 
                            }
                        )
                        count += 1
                    except KeyError as e:
                        self.stdout.write(self.style.ERROR(
                            f"KeyError: Coluna '{e}' ausente na linha do CSV para Departamento. Linha: {row}"
                        ))
                        continue
                        
                self.stdout.write(self.style.SUCCESS(f'{count} Departamentos importados/atualizados.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Erro: Arquivo '{filename}' não encontrado."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ocorreu um erro inesperado ao importar departamentos: {e}"))

   
    def importar_tecnologias(self):
        filename = CSV_DIR + 'tecnologias.csv'
        self.stdout.write(f'Importando Tecnologias de {filename}...')
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=CSV_DELIMITER)
                count = 0
                for row in reader:
                    row_data = {k.strip(): v.strip() if v is not None else '' 
                                for k, v in row.items() if k is not None}

                    if not row_data.get('nome'):
                        continue
                        
                    try:
                        Tecnologia.objects.get_or_create(
                            nome=row_data['nome'],
                            defaults={
                                'tipo': row_data.get('tipo'),
                                'versao': row_data.get('versao') or None, 
                                'fornecedor': row_data.get('fornecedor'),
                            }
                        )
                        count += 1
                    except KeyError as e:
                        self.stdout.write(self.style.ERROR(
                            f"KeyError: Coluna '{e}' ausente na linha do CSV para Tecnologia. Linha: {row}"
                        ))
                        continue
                        
                self.stdout.write(self.style.SUCCESS(f'{count} Tecnologias importadas/atualizadas.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Erro: Arquivo '{filename}' não encontrado."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ocorreu um erro inesperado ao importar tecnologias: {e}"))

   
    def importar_projetos(self):
        filename = CSV_DIR + 'projetos.csv'
        self.stdout.write(f'Importando Projetos de {filename}...')
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:

                reader = csv.DictReader(csvfile, delimiter=CSV_DELIMITER)

                count = 0
                for row in reader:
                    row_data = {k.strip(): v.strip() if v is not None else '' 
                                for k, v in row.items() if k is not None}
                    
                    if not row_data.get('nome'):
                        continue
                        
                    
                    departamento_nome = row_data.get('departamento_nome')
                    if not departamento_nome:
                        self.stdout.write(self.style.ERROR(
                            f"Erro de dados: 'departamento_nome' ausente ou vazio para o projeto '{row_data.get('nome', 'N/A')}'."
                        ))
                        continue
                        
                    try:
                        departamento = Departamento.objects.get(nome=departamento_nome)
                    except Departamento.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f"Departamento '{departamento_nome}' não encontrado para o projeto '{row_data.get('nome')}'."))
                        continue
                    except KeyError as e:
                        self.stdout.write(self.style.ERROR(
                            f"KeyError: Coluna '{e}' ausente na linha do CSV para Projeto. Linha: {row}"
                        ))
                        continue
                        
                    
                    try:
                        projeto, created = Projeto.objects.get_or_create(
                            nome=row_data['nome'],
                            defaults={
                                'descricao': row_data.get('descricao'),
                                'departamento': departamento,
                                'data_inicio': row_data.get('data_inicio'),
                                'data_fim': row_data.get('data_fim') or None,
                                'status': row_data.get('status'),
                            }
                        )
                    except KeyError as e:
                        self.stdout.write(self.style.ERROR(f"KeyError em campos obrigatórios do Projeto: Coluna '{e}' ausente. Linha: {row}"))
                        continue
                        
                    
                    tecnologias_nomes_str = row_data.get('tecnologias_nomes', '')
                    
                   
                    if tecnologias_nomes_str.upper() == 'N/A':
                        tecnologias_nomes_str = ''
                        
                    tecnologias_nomes = [t.strip() for t in tecnologias_nomes_str.split(';') if t.strip()]
                    
                    if tecnologias_nomes:
                        tecnologias_objs = Tecnologia.objects.filter(nome__in=tecnologias_nomes)
                        
                        
                        projeto.tecnologias.set(tecnologias_objs)
                    else:
                        projeto.tecnologias.clear()
                        
                    count += 1
                self.stdout.write(self.style.SUCCESS(f'{count} Projetos importados/atualizados.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Erro: Arquivo '{filename}' não encontrado."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ocorreu um erro inesperado ao importar projetos: {e}"))