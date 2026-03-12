# 9. Ambiente Docker — Instância PostgreSQL

Este documento descreve como o banco de dados PostgreSQL foi instanciado via Docker para o projeto **MoodTracker PUC**, incluindo os passos para subir o ambiente, rodar as migrações e conectar por um gerenciador de banco de dados.

---

## 9.1 Pré-requisitos

| Ferramenta | Versão mínima | Instalação |
|---|---|---|
| docker | 20.10+ | [docs.docker.com](https://docs.docker.com/engine/install/) |
| docker-compose | 1.26+ | [docs.docker.com/compose](https://docs.docker.com/compose/install/) |
| Python | 3.10+ | [python.org](https://www.python.org/downloads/) |

---

## 9.2 Estrutura de Arquivos

```
Sistema_Humor_PUC/
├── docker-compose.yml   ← definição do serviço PostgreSQL
├── .env.example         ← modelo de variáveis de ambiente (commitar)
├── .env                 ← variáveis locais reais        (NÃO commitar)
└── src/
    └── projeto/
        └── settings.py  ← Django lê o .env via python-dotenv
```

> ⚠️ O arquivo `.env` nunca deve ser commitado. Apenas o `.env.example` vai ao repositório.

---

## 9.3 Primeiros Passos — Subindo o Ambiente

### 1. Clonar e entrar na pasta do projeto
```bash
git clone <url-do-repositorio>
cd Sistema_Humor_PUC
```

### 2. Criar o arquivo `.env` local
```bash
cp .env.example .env
```
> Edite o `.env` se quiser trocar senha ou porta. Os valores padrão já funcionam para desenvolvimento.

### 3. Subir o container do banco
```bash
docker-compose up -d
```

### 4. Verificar se o container está saudável
```bash
docker-compose ps
```
Saída esperada:
```
Name              Command               State            Ports
---------------------------------------------------------------------------
humor_puc_db   docker-entrypoint.sh postgres   Up (healthy)   0.0.0.0:5433->5432/tcp
```

---

## 9.4 Migrações Django

Com o container rodando, entre na pasta `src/` e aplique as migrações:

```bash
cd src

# Gerar arquivos de migration (se houver mudanças nos models)
python manage.py makemigrations

# Aplicar todas as migrations no banco
python manage.py migrate
```

Saída esperada ao migrar pela primeira vez:
```
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
...
Applying core.0001_initial... OK
Applying sessions.0001_initial... OK
```

---

## 9.5 Validação da Instância pelo Terminal

### Listar bancos de dados disponíveis
```bash
docker exec -it humor_puc_db psql -U humor_user -d humor_db -c "\l"
```

### Listar todas as tabelas do projeto
```bash
docker exec -it humor_puc_db psql -U humor_user -d humor_db -c "\dt"
```

### Inspecionar a tabela principal do projeto
```bash
docker exec -it humor_puc_db psql -U humor_user -d humor_db -c "\d core_moodentry"
```

### Abrir o console interativo do psql
```bash
docker exec -it humor_puc_db psql -U humor_user -d humor_db
```

### Verificar o healthcheck do container
```bash
docker inspect --format='{{.Name}} → Health: {{.State.Health.Status}}' humor_puc_db
```

---

## 9.6 Conectar por um Gerenciador de Banco de Dados (GUI)

Use qualquer cliente PostgreSQL com as credenciais abaixo. Como o PostgreSQL nativo do sistema já ocupa a porta `5432`, o container é exposto na porta **`5433`**.

| Campo | Valor |
|---|---|
| **Host** | `localhost` |
| **Porta** | `5433` |
| **Banco** | `humor_db` |
| **Usuário** | `humor_user` |
| **Senha** | `humor_pass` |

### Clientes recomendados

| Cliente | Link | Observação |
|---|---|---|
| **DBeaver** | [dbeaver.io](https://dbeaver.io) | Gratuito, multi-plataforma |
| **TablePlus** | [tableplus.com](https://tableplus.com) | Interface moderna |
| **pgAdmin 4** | [pgadmin.org](https://www.pgadmin.org) | Oficial PostgreSQL |
| **VS Code** (extensão) | SQLTools + Driver PostgreSQL | Dentro do próprio editor |

### Exemplo de conexão no DBeaver
1. Abra o DBeaver → **New Database Connection** → selecione **PostgreSQL**
2. Preencha os campos conforme a tabela acima
3. Clique em **Test Connection** → deve retornar `Connected`
4. Clique em **Finish**

---

## 9.7 Variáveis de Ambiente (`.env.example`)

```dotenv
# PostgreSQL — usados pelo docker-compose e pelo Django
POSTGRES_DB=humor_db
POSTGRES_USER=humor_user
POSTGRES_PASSWORD=humor_pass
POSTGRES_HOST=localhost
POSTGRES_PORT=5433

# Django
DJANGO_SECRET_KEY=troque-por-uma-chave-segura
DJANGO_DEBUG=True
```

---

## 9.8 Comandos Úteis do dia a dia

| Ação | Comando |
|---|---|
| Subir o banco | `docker-compose up -d` |
| Parar o banco | `docker-compose down` |
| Ver logs do container | `docker-compose logs -f db` |
| Resetar volume (apaga dados!) | `docker-compose down -v` |
| Status + healthcheck | `docker-compose ps` |

---

## 9.9 Decisões Técnicas

- **PostgreSQL 16 Alpine** foi escolhido por ser a imagem oficial mais leve disponível.
- A porta do container foi mapeada para **`5433`** no host para evitar conflito com instâncias locais do PostgreSQL que ocupam a `5432` por padrão.
- O formato do `docker-compose.yml` usa **`version: "3.8"`**, compatível com `docker-compose 1.26+` sem exigir o Docker Compose V2 (`compose` plugin).
- As credenciais são injetadas via **`.env`** e lidas tanto pelo `docker-compose` quanto pelo Django através do `python-dotenv`.
