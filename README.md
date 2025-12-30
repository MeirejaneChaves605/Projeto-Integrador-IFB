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


🏦 InnovaBank - Gerenciador de Portfólio de TI
O InnovaBank é uma solução centralizada desenvolvida para a DigitalFlow Solutions. Trata-se de uma API moderna e segura projetada para gerenciar o portfólio de iniciativas de TI do banco, permitindo o controle de projetos, departamentos e tecnologias utilizadas em toda a organização.
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
   git clone https://github.com/seu-usuario/innovabank-api.git
cd innovabank-api

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
