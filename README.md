# Projeto-Integrador-IFB

Projeto Integrador realizado por:  
**Ester Luiza Souza Campos, Meirejane Figueredo Chaves e Naylanne Lissa Gomes Cunha**  
Curso **Backend - Python com Django** no **IFB/Riacho Fundo**

---

## Descrição do Projeto
O Projeto Integrador consistiu no desenvolvimento de uma API pela empresa **DigitalFlow Solutions** (empresa de tecnologia especializada em plataformas corporativas) 
para o banco de grande porte **InnovaBank**, que precisava de um sistema moderno para gerenciar seu portfólio interno de projetos de TI.

---

## Banco de Dados Conceitual e Logico

<img width="988" height="322" alt="image" src="https://github.com/user-attachments/assets/7bf2a247-efe7-4656-ac5d-f9186a107b14" />

---
<img width="1142" height="229" alt="image" src="https://github.com/user-attachments/assets/bd25d86e-15fe-4ec3-ab5f-038f0efe1fdb" />





## Como Iniciar a API

### 1. Abra a pasta innova_api na IDE (utilizamos VS Code)

### 2. Prepare o ambiente
No prompt cmd digite:

python -m venv meuAmbiente

meuAmbiente\Scripts\activate

---
### 3. Entre na pasta da API utilizando o comando:

cd innova_api
---

### 4. Instale os frameworks utilizando o seguinte comando:

pip install -r requirements.txt

---
### 5. Execute as migrações:

python manage.py makemigrations 

python manage.py migrate

---
### 6. E inicie a API através do comando:

python manage.py runserver

A API abre pelo link: http://127.0.0.1:8000/

---

### A API já conta com um usuário para acesso ao Django administration:

http://127.0.0.1:8000/admin/login/?next=/admin/login

Username: admin
Password: 123456
---

### 1. Para verificar se já existem usuários: 

python manage.py shell

from django.contrib.auth.models import User
User.objects.all()

<QuerySet []> os usuários aparecem aqui

Sair: exit ()
---
### 2. Para modificar a senha do usuário:
 
python manage.py changepassword <username>

No caso desse projeto:

python manage.py changepassword admin

Password: <preencha a nova senha>
---

### 3. Para criar um novo usuário principal:
---
python manage.py createsuperuser

Username:
Email:
Password:

### 4. Para criar usuários comuns:

python manage.py shell

from django.contrib.auth.models import User

User.objects.create_user(username="joao", password="123456")

---

### Para criar um token acesse:

http://localhost:8000/admin/

Authentication an authorization

Users/Add

Verifique em: 
http://127.0.0.1:8000/api/v1/token/

---

### Usar token no Swagger com JWT: Bearer SEU_TOKEN_AQUI

---

### Para ter acesso ao visual personalizado da API instale a extensão Live Server no VS Code e abra o arquivo index.html com botão direito/Open with Live Server.


🏦 Innova_api - Gerenciador de Portfólio de TI
O Innova_api é uma solução centralizada desenvolvida para a DigitalFlow Solutions. Trata-se de uma API moderna e segura projetada para gerenciar o portfólio de iniciativas de TI do banco, permitindo o controle de projetos, departamentos e tecnologias utilizadas em toda a organização.
🛠️ Descrição do Software
Este sistema foi construído para resolver a fragmentação de dados no banco. Ele permite que gestores controlem orçamentos, status de execução e riscos tecnológicos, enquanto fornece uma interface pública (interna) para consulta de dados via Dashboard ou ferramentas de BI.
Principais Funcionalidades:
 * Gestão de Projetos: CRUD completo de iniciativas com controle de status (Planejado, Em Execução, Concluído, Cancelado) e análise de risco.
 * Controle de Departamentos: Organização de áreas responsáveis por cada iniciativa.
 * Mapeamento Tecnológico: Registro de linguagens, frameworks e serviços cloud para análise de padrões.
 * Autenticação e Segurança: Endpoints de consulta são abertos, mas modificações exigem autenticação via JWT (JSON Web Token).
 * Integração de Dados: Comando customizado para importação massiva via arquivos CSV.
 * Exportação: Suporte para exportação de dados em formato CSV para ferramentas de auditoria.
🚀 Instalação e Configuração
Pré-requisitos
 * Python 3.10+
 * Gerenciador de pacotes pip
 * Virtualenv (recomendado)
Passo a Passo
 * Clone o repositório:
   git clone https://github.com/MeirejaneChaves605/Projeto-Integrador-IFB.git
cd innova_api

 * Crie e ative o ambiente virtual:
   python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

 * Instale as dependências:
   pip install -r requirements.txt

 * Execute as migrações do banco de dados:
   python manage.py migrate

 * Importe os dados iniciais (CSV):
   Certifique-se de que os arquivos .csv estejam na pasta portfolio/data/.
   python manage.py importaCSV

 * Crie um superusuário para acessar o Admin:
   python manage.py createsuperuser

 * Inicie o servidor:
   python manage.py runserver

📡 Documentação da API
A API utiliza o padrão REST e a documentação interativa pode ser acessada enquanto o servidor estiver rodando:
 * Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/
 * Esquema OpenAPI: /api/schema/
Endpoints Principais:
 * GET /api/v1/projetos/: Lista todos os projetos (Acesso Livre).
 * POST /api/v1/token/: Gera o token de acesso (JWT).
 * POST /api/v1/projetos/: Cria um novo projeto (Requer Autenticação).
🏗️ Modelo Lógico (Banco de Dados)
O banco de dados (SQLite em desenvolvimento) segue a seguinte estrutura:
 * Departamento: id, nome, gestor, descricao, ativo, data_criacao.
 * Tecnologia: id, nome, tipo, versao, fornecedor, descricao.
 * Projeto: id, nome, descricao, data_inicio, data_fim, status, risco, orcamento, departamento_id.
 * Relacionamento: Muitos-para-Muitos entre Projeto e Tecnologia.
💻 Tecnologias Utilizadas
 * Backend: Django & Django REST Framework
 * Autenticação: Simple JWT
 * Documentação: Drf-spectacular (Swagger)
 * Frontend: HTML5, CSS3 Moderno e Vanilla JavaScript
 * Banco de Dados: SQLite (padrão)
🔗 Links e Recursos
 * Painel Admin: /admin/
 * Frontend de Monitoramento: Localizado na pasta /frontend/ (Acesse home.html via Live Server).
> Nota: Este projeto faz parte do desafio "Bolsa Futuro Digital" do Instituto Federal de Brasília (IFB).

Innova_api - Gestão de Portfólio de TI
Instituições de Fomento e Parceria
Orientador e destaca-se:
Visão Geral
A InnovaBank API é uma solução robusta de backend desenvolvida para a centralização e governança do portfólio de projetos de TI do banco. O sistema permite o monitoramento de ciclos de vida de software, controle orçamentário e mapeamento de dependências tecnológicas, servindo como fonte de dados para dashboards executivos e auditorias de infraestrutura.
Problema que Resolve
Instituições financeiras frequentemente sofrem com a "Shadow IT" e a fragmentação de informações sobre projetos em andamento. A API resolve a falta de visibilidade sobre quais tecnologias estão sendo adotadas, o risco associado a cada iniciativa e a alocação orçamentária por departamento, substituindo planilhas manuais por um banco de dados relacional íntegro.
Objetivos Principais
 * Centralização Tecnológica: Mapear quais frameworks e linguagens são usados em cada projeto.
 * Gestão de Risco e Status: Monitorar o progresso das entregas e o nível de criticidade (Baixo a Crítico).
 * Transparência Orçamentária: Controlar os custos de hardware e software alocados a cada departamento.
 * Interoperabilidade: Fornecer dados via JSON para o frontend de monitoramento em tempo real.
Público-Alvo
 * CTOs e Gestores de TI: Para visão macro do portfólio.
 * Auditores: Para verificação de conformidade tecnológica.
 * Desenvolvedores: Para consulta de padrões de tecnologias adotadas pela empresa.
Funcionalidades de Alto Nível
 * CRUD de Projetos: Gestão completa com validação de datas e orçamentos.
 * Importação em Lote: Script customizado (importaCSV) para carga inicial de dados legados.
 * Exportação de Dados: Endpoints específicos para gerar relatórios em formato CSV.
 * Segurança JWT: Autenticação via tokens para operações de escrita (POST, PUT, DELETE).
 * Filtros Avançados: Busca por nome, status e ordenação cronológica via API.
Pacotes Utilizados
| Pacote | Versão | Descrição |
|---|---|---|
| django | 6.0 | Framework web principal |
| djangorestframework | latest | Toolkit para construção de APIs REST |
| djangorestframework-simplejwt | latest | Autenticação baseada em JSON Web Token |
| django-filter | latest | Filtragem de projetos por status e busca |
| drf-spectacular | latest | Geração automática de documentação Swagger/OpenAPI |
| django-cors-headers | latest | Permite a comunicação com o frontend separado |
Estrutura do Projeto
innova_api/
├── innova_api/ # Configurações globais (settings, urls)
├── portfolio/ # App principal de negócios
│ ├── management/ # Comandos customizados (importaCSV)
│ ├── models.py # Tabelas (Projeto, Departamento, Tecnologia)
│ ├── serializers.py # Transformação de dados para JSON
│ └── views.py # Lógica dos Endpoints
├── frontend/ # Interface web (HTML/JS/CSS)
├── static/ # Arquivos estáticos
├── manage.py
└── db.sqlite3

Documentação da API
A documentação interativa está disponível em /api/v1/schema/swagger-ui/.
Endpoints Principais
| Método | Endpoint | Descrição | Autenticação |
|---|---|---|---|
| GET | /api/v1/projetos/ | Lista todos os projetos de TI | Livre |
| POST | /api/v1/token/ | Obtém token JWT (Login) | Livre |
| POST | /api/v1/projetos/ | Cria novo projeto | Token JWT |
| GET | /api/v1/departamentos/ | Lista departamentos do banco | Livre |
| GET | /api/v1/tecnologias/ | Lista stack tecnológica permitida | Livre |
Configuração do Ambiente
 * Clone e entre na pasta:
   git clone https://github.com/MeirejaneChaves605/Projeto-Integrador-IFB.git
cd Innova_api

 * Crie o ambiente virtual e instale as dependências:
   python -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate
pip install -r requirements.txt

 * Migre o banco e importe os dados:
   python manage.py migrate
python manage.py importaCSV # Popula o banco com os CSVs iniciais

 * Inicie o serviço:
   python manage.py runserver

Desenvolvido como projeto integrador para o InnovaBank.
Estudante: [Seu Nome]
Orientador: Henrique Freitas
O que eu fiz de diferente para você:
 * Badges Atualizadas: Coloquei as versões corretas conforme o seu settings.py (Django 6.0).
 * Pacotes Específicos: Adicionei o simplejwt e cors-headers que estão no seu código mas não estavam no modelo anterior.
 * Endpoints Reais: Ajustei os caminhos para usarem o prefixo /api/v1/ que está no seu urls.py.
 * Comando Customizado: Destaquei o importaCSV, que é um diferencial do projeto.

Innova_api - Gestão de Portfólio de TI
Instituições de Fomento e Parceria
Orientador
Visão Geral
A Innova_api é uma solução de backend RESTful desenvolvida para a centralização e governança do portfólio de projetos de TI do banco. O sistema permite o monitoramento de ciclos de vida de software, controle orçamentário e mapeamento de dependências tecnológicas.
Funcionalidades de Alto Nível
 * CRUD de Projetos: Gestão com controle de status e análise de risco.
 * Importação em Lote: Script customizado (importaCSV) para carga inicial de dados.
 * Exportação CSV: Endpoints para extração de dados de departamentos e tecnologias.
 * Segurança JWT: Autenticação protegida para operações de escrita.
Estrutura do Projeto
innova_api/
├── innova_api/ # Configurações globais
├── portfolio/ # App principal
│ ├── management/ # Script de importação CSV
│ ├── models.py # Projeto, Departamento, Tecnologia
│ └── views.py # Lógica dos Endpoints
├── frontend/ # Interface HTML/JS/CSS
└── manage.py

Diagrama de Banco de Dados
Abaixo está a representação visual do modelo de dados implementado no models.py:
erDiagram
    DEPARTAMENTO ||--o{ PROJETO : "possui"
    PROJETO }o--o{ TECNOLOGIA : "utiliza"

    DEPARTAMENTO {
        int id
        string nome
        string gestor
        text descricao
        boolean ativo
        datetime data_criacao
    }

    PROJETO {
        int id
        string nome
        text descricao
        date data_inicio
        date data_fim
        string status
        string risco
        decimal orcamento
        datetime data_criacao
    }

    TECNOLOGIA {
        int id
        string nome
        string tipo
        string versao
        string fornecedor
        text descricao
    }

> Descrição: O sistema utiliza uma relação de 1:N entre Departamentos e Projetos, e uma relação N:N (Many-to-Many) entre Projetos e Tecnologias para rastrear a stack técnica de cada iniciativa.
> 
Documentação da API
| Método | Endpoint | Descrição | Autenticação |
|---|---|---|---|
| GET | /api/v1/projetos/ | Lista projetos de TI | Livre |
| POST | /api/v1/token/ | Obtém token JWT (Login) | Livre |
| POST | /api/v1/projetos/ | Cria novo projeto | Token JWT |
| GET | /api/v1/departamentos/ | Lista departamentos | Livre |
Configuração do Ambiente
 * Instalação:
   git clone https://github.com/SeuUsuario/InnovaBank.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

 * Carga de Dados:
   python manage.py migrate
python manage.py importaCSV

 * Execução:
   python manage.py runserver

* Desenvolvido por: Ester Luiza Souza Campos, Meirejane Figueredo Chaves e Naylanne Lissa Gomes Cunha
* Orientador: Henrique Freitas (IFB)

