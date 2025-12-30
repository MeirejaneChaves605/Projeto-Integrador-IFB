const API_URL_BASE = 'http://127.0.0.1:8000/api/v1/';
const PROJECTS_URL = `${API_URL_BASE}projetos/`;
const TOKEN_AUTH_URL = `${API_URL_BASE}auth/token/login/`; 
const TOKEN_STORAGE_KEY = 'innovaBankAuthToken';
const USERNAME_STORAGE_KEY = 'innovaBankUsername';
const DEPARTMENTS_URL = `${API_URL_BASE}departamentos/`;
const TECHNOLOGIES_URL = `${API_URL_BASE}tecnologias/`;
const BASE_URL = 'http://127.0.0.1:8000';
const DEPARTMENTS_CSV_URL = `${API_URL_BASE}departamentos/export_csv/`;
const TECHNOLOGIES_CSV_URL = `${API_URL_BASE}tecnologias/export_csv/`;



/**
 @param {string} status 
 @returns {string} 
 */
function getStatusClass(status) {
    switch (status) {
        case 'Concluido':
            return 'status-concluido';
        case 'Em Execução':
            return 'status-execucao';
        case 'Planejado':
            return 'status-planejado';
        case 'Cancelado':
            return 'status-cancelado';
        default:
            return '';
    }
}

/**
 @returns {string} 
 */
function buildQueryURL() {
    const status = document.getElementById('status-filter').value;
    const search = document.getElementById('search').value;
    const ordering = document.getElementById('ordering-select').value;

    const params = new URLSearchParams();

    if (status) {
        params.append('status', status);
    }
    
    if (search) {
        params.append('search', search);
    }

    if (ordering) {
        params.append('ordering', ordering);
    }

    return `${PROJECTS_URL}?${params.toString()}`;
}
/**
 */
function checkAuthStatus() {
    const token = localStorage.getItem(TOKEN_STORAGE_KEY);
    const username = localStorage.getItem(USERNAME_STORAGE_KEY);
    const authMessage = document.getElementById('auth-message');

    authMessage.textContent = ''; 

    if (token) {
        
        document.getElementById('login-form-container').style.display = 'none';
        document.getElementById('logout-container').style.display = 'block';
        document.getElementById('logged-user').textContent = username;
    } else {
        
        document.getElementById('login-form-container').style.display = 'block';
        document.getElementById('logout-container').style.display = 'none';
        document.getElementById('logged-user').textContent = '';
    }
}
/**
 */
async function handleLogin() {
    const usernameInput = document.getElementById('username').value;
    const passwordInput = document.getElementById('password').value;
    const authMessage = document.getElementById('auth-message');

    authMessage.textContent = 'Autenticando...';
    authMessage.style.color = 'blue';

    try {
        const response = await fetch(TOKEN_AUTH_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: usernameInput,
                password: passwordInput
            })
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({ non_field_errors: ['Erro desconhecido ou resposta não é JSON.'] }));

            const errorMessage = errorData.non_field_errors ? errorData.non_field_errors[0] : 'Erro de credenciais.';
            authMessage.textContent = `Falha no Login: ${errorMessage}`;
            authMessage.style.color = 'red';
            return;
        }

        const data = await response.json();
        const token = data.token;

        localStorage.setItem(TOKEN_STORAGE_KEY, token);
        localStorage.setItem(USERNAME_STORAGE_KEY, usernameInput);

        checkAuthStatus();
        authMessage.textContent = 'Login bem-sucedido! A página será recarregada automaticamente na próxima vez.';
        authMessage.style.color = 'green';
        
        
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';


        fetchAndRenderProjects();

    } catch (error) {
        console.error('Erro de rede ou na API:', error);
        authMessage.textContent = 'Erro ao conectar com o servidor. Verifique o console e se o Django está rodando.';
        authMessage.style.color = 'red';
    }
}

/**
 */
function handleLogout() {
    localStorage.removeItem(TOKEN_STORAGE_KEY);
    localStorage.removeItem(USERNAME_STORAGE_KEY);
    checkAuthStatus();
    document.getElementById('auth-message').textContent = 'Sessão encerrada. Permissão de escrita removida.';
    document.getElementById('auth-message').style.color = 'black';
    fetchAndRenderProjects();
}

/**
 */
async function fetchAndRenderProjects() {
    const tableBody = document.querySelector('#projects-table tbody');
    const projectCountSpan = document.getElementById('project-count');
    const url = buildQueryURL();

    tableBody.innerHTML = '<tr><td colspan="6">Carregando projetos...</td></tr>';
    projectCountSpan.textContent = '0';

    try {
        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`Erro na API: ${response.statusText}`);
        }

        const projects = await response.json(); 

        projectCountSpan.textContent = projects.length;
        
        if (projects.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="6">Nenhum projeto encontrado com os filtros aplicados.</td></tr>';
            return;
        }

        tableBody.innerHTML = ''; 

        projects.forEach(projeto => {
            const row = tableBody.insertRow();
            
            
            row.insertCell().textContent = projeto.id;
            
            const nameCell = row.insertCell();
            nameCell.textContent = projeto.nome;
            nameCell.title = projeto.descricao; 
            
            
            const deptName = projeto.departamento && projeto.departamento.nome ? projeto.departamento.nome : projeto.departamento;
            row.insertCell().textContent = deptName || 'N/A';
            
            
            const statusCell = row.insertCell();
            statusCell.innerHTML = `<span class="status-badge ${getStatusClass(projeto.status)}">${projeto.status}</span>`;
            
            
            row.insertCell().textContent = projeto.data_inicio;
            
            
            const techCell = row.insertCell();
            if (projeto.tecnologias && projeto.tecnologias.length > 0) {
                
                techCell.innerHTML = projeto.tecnologias.map(tech => 
                    `<span class="tech-tag">${tech.nome}</span>`
                ).join('');
            } else {
                techCell.textContent = 'Nenhuma';
            }
        });

    } catch (error) {
        console.error('Falha ao buscar projetos:', error);
        tableBody.innerHTML = `<tr><td colspan="6" style="color: red;">Erro ao carregar dados. Verifique se o servidor Django está rodando em ${PROJECTS_URL}.</td></tr>`;
    }
}

/**
 */
async function fetchAndRenderDepartments() {
    const listContainer = document.getElementById('departamentos-list');
    
    if (!listContainer) return; 

    listContainer.innerHTML = '<li>Carregando departamentos...</li>';

    try {
        const response = await fetch(DEPARTMENTS_URL);
        const departments = await response.json();

        listContainer.innerHTML = '';
        
        if (departments.length === 0) {
            listContainer.innerHTML = '<li>Nenhum departamento encontrado.</li>';
            return;
        }

        departments.forEach(dept => {
            const listItem = document.createElement('li');
            listItem.innerHTML = `<strong>ID ${dept.id}:</strong> ${dept.nome} 
                                  <span style="color: #666;">(${dept.descricao})</span>`;
            listContainer.appendChild(listItem);
        });

    } catch (error) {
        console.error('Erro ao buscar departamentos:', error);
        listContainer.innerHTML = '<li>Erro ao carregar departamentos. Verifique a API.</li>';
    }
}
/**
 */
async function fetchAndRenderTechnologies() {
    const listContainer = document.getElementById('tecnologias-list');
    
    if (!listContainer) return;

    listContainer.innerHTML = '<li>Carregando tecnologias...</li>';

    try {
        const response = await fetch(TECHNOLOGIES_URL);
        const technologies = await response.json();

        listContainer.innerHTML = ''; 
        
        if (technologies.length === 0) {
            listContainer.innerHTML = '<li>Nenhuma tecnologia encontrada.</li>';
            return;
        }

        technologies.forEach(tech => {
            const listItem = document.createElement('li');
            listItem.textContent = `ID ${tech.id}: ${tech.nome}`;
            listContainer.appendChild(listItem);
        });

    } catch (error) {
        console.error('Erro ao buscar tecnologias:', error);
        listContainer.innerHTML = '<li>Erro ao carregar tecnologias. Verifique a API.</li>';
    }
}
/**
 */
function fixExternalLinks() {
    document.querySelectorAll('.extra-links a').forEach(link => {
        const href = link.getAttribute('href');
        if (href && href.startsWith('/') && !href.startsWith('/api/v1/frontend/')) {
            link.setAttribute('href', BASE_URL + href);
        }
    });
}
/**
 */
function exportDepartamentosCSV() {
    
    window.open(DEPARTMENTS_CSV_URL, '_blank');
}

/**
 */
function exportTecnologiasCSV() {
    window.open(TECHNOLOGIES_CSV_URL, '_blank');
}


document.addEventListener('DOMContentLoaded', () => {
    
    checkAuthStatus();
    fixExternalLinks();
    fetchAndRenderProjects();
    fetchAndRenderDepartments();
    fetchAndRenderTechnologies(); 


    document.getElementById('login-button').addEventListener('click', handleLogin);
    document.getElementById('logout-button').addEventListener('click', handleLogout);
    document.getElementById('apply-filters').addEventListener('click', fetchAndRenderProjects);
    document.getElementById('status-filter').addEventListener('change', fetchAndRenderProjects);
    document.getElementById('ordering-select').addEventListener('change', fetchAndRenderProjects);
    document.getElementById('search').addEventListener('keyup', (e) => {
        if (e.key === 'Enter') {
            fetchAndRenderProjects();
        }
    });
    
    const exportDeptButton = document.getElementById('export-departamentos-csv');
    if (exportDeptButton) {
        exportDeptButton.addEventListener('click', exportDepartamentosCSV);
    }
    
    const exportTechButton = document.getElementById('export-tecnologias-csv');
    if (exportTechButton) {
        exportTechButton.addEventListener('click', exportTecnologiasCSV);
    }
    
});