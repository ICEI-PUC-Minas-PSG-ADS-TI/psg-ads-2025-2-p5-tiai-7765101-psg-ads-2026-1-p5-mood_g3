# Guia de Onboarding — MOODLY (Mood Tracker)

Guia técnico interno para a equipe de desenvolvimento.

---

## Sobre o Projeto

| Item            | Detalhe                                |
| --------------- | -------------------------------------- |
| **Arquitetura** | MVT (Model – View – Template)          |
| **Back-end**    | Django 4.x · Python 3.10+             |
| **Front-end**   | Bootstrap 5 (via CDN)                 |
| **Banco**       | SQLite (dev) — facilmente substituível |

O usuário autenticado pode registrar seu humor diário escolhendo uma **emoção** (Happy, Sad, Neutral, Anxious, Stressed), definir a **intensidade** (1–10) e adicionar **observações** livres. O Dashboard apresenta o histórico de registros com barra de progresso visual.

---

## Organização do Projeto — Onde Codar

```
Sistema_Humor_PUC/
├── README.md               ← README oficial (template PUC)
├── docs/                   ← Documentação acadêmica + este guia
├── requirements.txt        ← Dependências Python
│
└── src/                    ← 🔧 TODO o código Django fica aqui
    ├── manage.py
    ├── projeto/            ← Configurações globais (settings, urls raiz)
    │
    ├── core/               ← Back-end — Separação de responsabilidades
    │   ├── models.py       → Modelagem de dados
    │   ├── views.py        → Lógica de apresentação (recebe request, retorna response)
    │   ├── services.py     → Lógica de negócio (regras isoladas das views)
    │   ├── serializers.py  → Serialização de dados (API / JSON)
    │   ├── forms.py        → Formulários com widgets Bootstrap
    │   ├── urls.py         → Rotas do app
    │   ├── admin.py        → Configuração do painel administrativo
    │   ├── managers.py     → QuerySets customizados
    │   ├── signals.py      → Sinais do Django (hooks pós-save, etc.)
    │   └── tests.py        → Testes unitários
    │
    ├── templates/          ← Front-end — Todos os HTMLs
    │   ├── base.html       → Layout global (navbar, Bootstrap, blocks)
    │   ├── core/           → Templates do app core
    │   └── registration/   → Templates de autenticação
    │
    └── static/             → Arquivos estáticos (CSS, JS, imagens)
        ├── css/
        ├── js/
        └── images/
```

> **Regra de Ouro:** Back-end (`src/core/`) e Front-end (`src/templates/`) vivem em pastas separadas. Cada app possui sua subpasta dentro de `templates/`. Isso evita conflitos quando múltiplos devs trabalham em paralelo.

---

## Guia de Instalação Rápida

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd Sistema_Humor_PUC
```

### 2. Criar a VENV

```bash
python -m venv venv
```

### 3. Ativar a VENV

**Linux / macOS:**

```bash
source venv/bin/activate
```

**Windows (CMD):**

```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Entrar na pasta do código-fonte

```bash
cd src
```

### 6. Criar o banco de dados local

```bash
python manage.py migrate
```

### 7. Criar o superusuário

```bash
python manage.py createsuperuser
```

### 8. Rodar o servidor local

```bash
python manage.py runserver
```

---

## Rotina Diária

```bash
source venv/bin/activate   # Linux/Mac  (Windows: venv\Scripts\activate)
cd src
python manage.py runserver
```

---

## Acesso

| Recurso          | URL                                                          |
| ---------------- | ------------------------------------------------------------ |
| **Sistema**      | [http://127.0.0.1:8000](http://127.0.0.1:8000)              |
| **Painel Admin** | [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)  |
| **Login**        | [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login)  |

---

## Boas Práticas de Git

```text
   NUNCA commite diretamente na branch main.
```

1. **Crie uma branch** antes de começar qualquer tarefa:

   ```bash
   git checkout -b feature/nome-da-sua-tarefa
   ```

2. **Faça commits pequenos e descritivos:**

   ```bash
   git add .
   git commit -m "feat: adiciona filtro por emoção no dashboard"
   ```

3. **Suba a branch e abra um Pull Request:**

   ```bash
   git push origin feature/nome-da-sua-tarefa
   ```

4. **Só faça merge na `main` após revisão** de pelo menos um colega.

> **Dica:** Use prefixos nos commits → `feat:` (nova feature), `fix:` (correção), `refactor:` (refatoração), `docs:` (documentação).
