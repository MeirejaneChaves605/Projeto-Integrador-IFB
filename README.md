# Projeto-Integrador-IFB

# Este projeto é o seguinte: 

<img align="center" width="800px" style="margin-top:-20px" src="https://github.com/MeirejaneChaves605/ExerciciosAulaPythonIFB/blob/main/imagem/Imagem1.jpg?raw=true.png">

# Projeto Integrador

# Contexto de Negócio

* Você foi contratado como desenvolvedor backend pela DigitalFlow
Solutions, uma empresa de tecnologia especializada em criar plataformas
corporativas para grandes organizações. O novo cliente da DigitalFlow é a
InnovaBank, um banco de grande porte que está passando por uma
transformação digital e precisa de um sistema moderno para gerenciar seu
portfólio interno de projetos de TI.
* Hoje, o banco possui dezenas de iniciativas simultâneas, distribuídas
entre vários departamentos (TI, Segurança, Dados, Infraestrutura, CRM etc.).
Cada projeto utiliza diversas tecnologias como Python, Java, Angular,
PostgreSQL e outras. A diretoria quer uma API centralizada, segura e
documentada para alimentar dashboards estratégicos, integrar com outros
sistemas e permitir o gerenciamento interno. Você fará parte da equipe que
entregará essa API.
* A solução será implantada dentro da área de Gestão de Portfólio (PMO
de Tecnologia) do InnovaBank. A área precisa:
• Consultar publicamente (de forma interna ao banco) todos os projetos
em andamento e concluídos;
• Permitir que apenas gestores autorizados possam registrar novos
projetos, atualizar status, encerrar, editar orçamento e excluir registros
obsoletos;
• Gerenciar de forma consistente as tecnologias utilizadas em cada
projeto, permitindo análise de padrões tecnológicos do banco;
• Saber quais tecnologias são mais utilizadas, comparar departamentos e
controlar riscos tecnológicos.
* Essa API será consumida por: painéis internos do banco (PowerBI,
Tableau), aplicações internas de gestão, ferramentas de auditoria e
ferramentas de governança de TI. Por isso, qualidade, segurança e
organização são requisitos obrigatórios.

# Modelagem das Entidades e Colunas

* A API deverá gerenciar três entidades essenciais para a governança do
banco:
• Departamento: Representa áreas internas responsáveis por projetos de
TI. Colunas da tabela: id, nome, gestor, descrição, ativo (indica se está
ativo) e data de criação (registro automático);
• Projeto: Cada iniciativa de TI em execução ou concluída. Colunas da
tabela: id, nome, descrição, departamento responsável, data de início,
data do fim e status (“Planejado”, “Em Execução”, “Concluído” e
“Cancelado”);
• Tecnologia: Todas as tecnologias oficialmente usadas em projetos do
banco. Colunas da tabela: id, nome (Ex: “Python”, “Angular”, “AWS
Lambda”), tipo (Linguagem, Framework, Serviço Cloud etc.), versão,
fornecedor (Ex: Oracle, Amazon, Google, Red Hat) e descrição.
Um projeto está vinculado a um departamento e um departamento pode
ter vários projetos. Uma tecnologia pode ser utilizada em vários projetos e um
projeto pode utilizar várias tecnologias.

# Regras de Acesso e Filtros

* Seguindo as políticas do InnovaBank:
• GET – Acesso liberado (sem autenticação): Todos podem visualizar
informações, pois são dados internos de consulta geral:
◦ /departamentos/
◦ /projetos/
◦ /tecnologias/
• POST, PUT, DELETE – Acesso restrito (com autenticação): Somente
usuários autenticados e autorizados (gestores, PMO, TI) podem alterar
dados, como por exemplo:
◦ Criar novo projeto;
◦ Alterar status ou orçamento;
◦ Registrar nova tecnologia;
◦ Encerrar departamento inativo.
* O PMO precisa de filtros para análises rápidas, como por exemplo:
• Projetos por departamento;
• Projetos com risco “Alto”;
• Projetos iniciados entre duas datas;
• Projetos que utilizam determinada tecnologia;
• Tecnologias por tipo (linguagens, frameworks etc.);
• Departamentos ativos/inativos.
* Esses filtros serão usados por ferramentas de BI e auditoria interna.

# Entrega do Projeto

* Deve ser entregue o repositório GitHub com o código completo do projeto e o
README com os seguintes tópicos:
• Descrição do Software;
• Instalação e Configuração (passo a passo para instalação e
configuração do sofware);
• Documentação da API (recomendado usar Swagger);
• Modelo Lógico do Banco de dados (Modelo Relacional);
• Link da Publicação da Aplicação (opcional, mas recomendado).

Projeto Integrador realizado por:  
**Ester Luiza Souza Campos, Meirejane Figueredo Chaves e Naylanne Lissa Gomes Cunha**  
Curso **Backend - Python com Django** no **IFB/Riacho Fundo**

---
# 🏦 Innova_api - Gerenciador de Portfólio de TI

O Innova_api é uma solução centralizada desenvolvida para a DigitalFlow Solutions. Trata-se de uma API moderna e segura projetada para gerenciar o portfólio de iniciativas de TI do banco, permitindo o controle de projetos, departamentos e tecnologias utilizadas em toda a organização.

## 🛠️ Descrição do Software
Este sistema foi construído para resolver a fragmentação de dados no banco. Ele permite que gestores controlem orçamentos, status de execução e riscos tecnológicos, enquanto fornece uma interface pública (interna) para consulta de dados via Dashboard ou ferramentas de BI.
O Projeto Integrador consistiu no desenvolvimento de uma API pela empresa **DigitalFlow Solutions** (empresa de tecnologia especializada em plataformas corporativas) 
para o banco de grande porte **InnovaBank**, que precisava de um sistema moderno para gerenciar seu portfólio interno de projetos de TI.

---

# API do Projeto

[![Python](https://img.shields.io/badge/Python-3.13.5%2B-blue.svg?logo=python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.0%2B-green.svg?logo=Django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## Parcerias e instituições
[![Website IFB](https://img.shields.io/badge/Website-IFB-%23508C3C.svg?labelColor=%23C8102E)](https://www.ifb.edu.br/) 
[![Website ihwbr](https://img.shields.io/badge/Website-ihwbr-%23DAA520.svg?labelColor=%232E2E2E)](https://hardware.org.br/)

## Orientador (Professor)

[![LinkedIn Henrique Pereira](https://img.shields.io/badge/LinkedIn-Henrique_Freitas-%230077B5.svg?labelColor=%23FFFFFF&logo=linkedin)](https://br.linkedin.com/in/henrique-freitas-69b836b4)
[![GitHub Henrique](https://img.shields.io/badge/GitHub-henriquepff_(Henrique_Freitas)-%23181717.svg?logo=github&logoColor=white)](https://github.com/henriquepff/)
[![Lattes Henrique Pereira](https://img.shields.io/badge/Lattes-Henrique_Freitas-green.svg?logo=cnpq&logoColor=white)](https://buscatextual.cnpq.br/buscatextual/visualizacv.do;jsessionid=8B62CFB2D86DC88AE42BDFC0BF85BBBE.buscatextual_0)


## Banco de Dados Conceitual e Logico

<img width="988" height="322" alt="image" src="https://github.com/user-attachments/assets/7bf2a247-efe7-4656-ac5d-f9186a107b14" />

---
<img width="1142" height="229" alt="image" src="https://github.com/user-attachments/assets/bd25d86e-15fe-4ec3-ab5f-038f0efe1fdb" />

# Principais Funcionalidades:
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
 * Swagger UI: http://127.0.0.1:8000/api/docs/
 * Esquema OpenAPI: /api/schema/
Endpoints Principais:
 * GET /api/v1/projetos/: Lista todos os projetos (Acesso Livre).
 * POST /api/v1/token/: Gera o token de acesso (JWT).
 * POST /api/v1/projetos/: Cria um novo projeto (Requer Autenticação).



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

# 🏗️ Modelo Lógico (Banco de Dados)
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

```text
innova_api_root/
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/
│   ├── management/
│   │   └── commands/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── admin.py
│   └── urls.py
├── frontend/
├── static/
├── README.md
├── requirements.txt
├── manage.py
└── db.sqlite3
```

# requirements.txt

```text
django>=5.0,<6.0
djangorestframework
djangorestframework-simplejwt
django-filter
drf-spectacular
django-cors-headers
```

# Innova_api 🚀

API de Gestão de Portfólio com filtros avançados, autenticação JWT e documentação automática.



## ⚙️ Funcionalidades
- **Busca Avançada:** Filtros por nome, status e ordenação cronológica.
- **Gestão:** CRUD de Projetos, Departamentos e Tecnologias.
- **Docs:** Documentação interativa via Swagger.
- **Segurança:** Proteção de endpoints via JWT e suporte a CORS.

## 🚀 Como Executar
1. Clone o repositório: `git clone <url-do-repo>`
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o venv e instale as dependências: `pip install -r requirements.txt`
4. Execute as migrações: `python manage.py migrate`
5. Inicie o servidor: `python manage.py runserver`

> Nota: Este projeto faz parte do desafio "Bolsa Futuro Digital" do Instituto Federal de Brasília (IFB).


# 🏦 Innova_api - Gerenciador de Portfólio de TI

# 📌 Sumário

- [Visão Geral](#visão-geral)
- [Problema que Resolve](#problema-que-resolve)
- [Objetivos Principais](#objetivos-principais)
- [Público Alvo](#público-alvo)
- [Funcionalidades de Alto Nível](#funcionalidades-de-alto-nível)
- [Pacotes Utilizados](#pacotes-utilizados)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Diagrama de Banco de Dados](#diagrama-de-banco-de-dados)
- [Documentação da API](#documentação-da-api)
- [Configuração do Ambiente](#configuração-do-ambiente)

#  Visão Geral
A Innova_api é uma solução robusta de backend desenvolvida para a centralização e governança do portfólio de projetos de TI do banco. O sistema permite o monitoramento de ciclos de vida de software, controle orçamentário e mapeamento de dependências tecnológicas, servindo como fonte de dados para dashboards executivos e auditorias de infraestrutura.
#  Problema que Resolve
Instituições financeiras frequentemente sofrem com a "Shadow IT" e a fragmentação de informações sobre projetos em andamento. A API resolve a falta de visibilidade sobre quais tecnologias estão sendo adotadas, o risco associado a cada iniciativa e a alocação orçamentária por departamento, substituindo planilhas manuais por um banco de dados relacional íntegro.
#  Objetivos Principais
 * Centralização Tecnológica: Mapear quais frameworks e linguagens são usados em cada projeto.
 * Gestão de Risco e Status: Monitorar o progresso das entregas e o nível de criticidade (Baixo a Crítico).
 * Transparência Orçamentária: Controlar os custos alocados a cada departamento.
 * Interoperabilidade: Fornecer dados via JSON para o frontend de monitoramento em tempo real.
   
#  Público Alvo
 * CTOs e Gestores de TI: Para visão macro do portfólio.
 * Auditores: Para verificação de conformidade tecnológica.
 * Desenvolvedores: Para consulta de padrões de tecnologias adotadas pela empresa.
   
#  Funcionalidades de Alto Nível
 * CRUD de Projetos: Gestão completa com validação de datas e orçamentos.
 * Importação em Lote: Script customizado (importaCSV) para carga inicial de dados legados via terminal.
 * Exportação de Dados: Endpoints específicos para gerar relatórios em formato CSV de Departamentos e Tecnologias.
 * Segurança JWT: Autenticação via tokens (Simple JWT) para operações de escrita.
 * Filtros Avançados: Busca por nome, status e ordenação cronológica diretamente via parâmetros de URL.
   
#  Pacotes Utilizados
| Pacote | Versão | Descrição |
|---|---|---|
| Django | 6.0 | Framework Web principal. |
| Django REST Framework | Latest | Toolkit para construção da API. |
| Simple JWT | Latest | Autenticação segura via tokens. |
| Django Filter | Latest | Motor de busca e filtragem dinâmica. |
| DRF Spectacular | Latest | Geração de documentação Swagger UI. |
| CORS Headers | Latest | Permite integração entre domínios (Frontend/Backend). |

#  Estrutura do Projeto
* O projeto é dividido entre uma API RESTful e um cliente web estático.
  
```text
 Backend
backend/
├── innova_api/ # Configurações do projeto Django
├── portfolio/ # Aplicação de negócios
│ ├── management/ # Comandos customizados (importaCSV.py)
│ ├── data/ # CSVs para importação inicial
│ ├── models.py # Tabelas (Projeto, Departamento, Tecnologia)
│ ├── serializers.py # Lógica de conversão JSON
│ ├── urls.py # Endpoints da API v1
│ └── views.py # Lógica de processamento
├── db.sqlite3 # Banco de dados local
└── requirements.txt # Dependências Python

```
```text
 Frontend
frontend/
├── index.html # Interface de usuário (Dashboard)
├── style.css # Estilização e responsividade
├── script.js # Lógica de consumo da API e Auth
└── src/imagens/ # Assets visuais (Logo e background)

```

# Documentação da API
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



# Diagrama de Banco de Dados
Abaixo está a representação visual do modelo de dados implementado no models.py:
  ```text
erDiagram
    DEPARTAMENTO ||--o{ PROJETO : "possui"
    PROJETO }o--o{ TECNOLOGIA : "utiliza"
```

  #  DEPARTAMENTO {
        int id
        string nome
        string gestor
        text descricao
        boolean ativo
        datetime data_criacao
    }

   # PROJETO {
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

   # TECNOLOGIA {
        int id
        string nome
        string tipo
        string versao
        string fornecedor
        text descricao
    }

> Descrição: O sistema utiliza uma relação de 1:N entre Departamentos e Projetos, e uma relação N:N (Many-to-Many) entre Projetos e Tecnologias para rastrear a stack técnica de cada iniciativa.
> 
# Documentação da API
| Método | Endpoint | Descrição | Autenticação |
|---|---|---|---|
| GET | /api/v1/projetos/ | Lista projetos de TI | Livre |
| POST | /api/v1/token/ | Obtém token JWT (Login) | Livre |
| POST | /api/v1/projetos/ | Cria novo projeto | Token JWT |
| GET | /api/v1/departamentos/ | Lista departamentos | Livre |
# A API utiliza o padrão OpenAPI 3.0. Com o servidor rodando, acesse:
 * Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/
 * Admin Django: http://127.0.0.1:8000/admin/

# Configuração do Ambiente
 * Instalação:
   git clone https://github.com/MeirejaneChaves605/Projeto-Integrador-IFB.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

 * Carga de Dados:
   python manage.py migrate
python manage.py importaCSV

 * Execução:
python manage.py runserver
* Configure o Backend:
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py importaCSV
python manage.py runserver

 
* # Desenvolvido por: Ester Luiza Souza Campos, Meirejane Figueredo Chaves e Naylanne Lissa Gomes Cunha
* # Orientador: Henrique Freitas (IFB)

