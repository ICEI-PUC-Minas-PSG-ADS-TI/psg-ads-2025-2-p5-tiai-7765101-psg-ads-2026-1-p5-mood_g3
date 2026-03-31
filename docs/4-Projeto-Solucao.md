
# 4. Projeto da Solução

> ⚠️ **Aviso aos Squads (Software House)**
>
> Esta seção **não deve ser preenchida integralmente antes da codificação**.
> Trata-se de um **Documento Vivo**, que deverá ser atualizado **incrementalmente a cada Sprint**, refletindo fielmente o código real implementado.

---

## 4.1 Arquitetura da Solução (Sprint 1 e 2)

Apresente um **diagrama macro** demonstrando como os componentes do sistema se comunicam.

A arquitetura deve refletir o modelo de **fatias verticais**, evidenciando o fluxo:

**Front-end → API (Back-end) → Banco de Dados**

Semelhante à imagem abaixo:

![Exemplo de Arquitetura](https://uds.com.br/blog/wp-content/uploads/2024/09/Imagem-1-Comparativo-ilustrativo-das-diferencas-entre-front-end-e-back-end.jpg)



 **Fonte:** [Guia Completo de Desenvolvimento de Software - UDS](https://uds.com.br/blog/desenvolvimento-de-software-guia-completo/) <br><br>
 
 ### 📎 Inserir o Diagrama de Arquitetura do Projeto do Grupo
🚨 O grupo deverá inserir aqui a imagem


---
🔧**Ferramentas recomendadas:**
- Draw.io
- Lucidchart
- Figma

---

## 4.2 Tecnologias Utilizadas (Sprint 1)

Descreva as tecnologias, linguagens, frameworks, bibliotecas e serviços escolhidos pelo Squad.

| Dimensão | Tecnologia Escolhida |
|----------|----------------------|
| Banco de Dados (SGBD) | Ex: SQL Server, PostgreSQL ou MongoDB |
| Back-end (API) | Ex: C# (.NET Core) |
| Front-end / Mobile | Ex: HTML + CSS + JavaScript, React ou Flutter |
| Hospedagem / Deploy | Ex: Azure, AWS, Render ou Railway |
| Gestão e Versionamento | GitHub e GitHub Projects (Kanban) |

 ⚠️ **Observação:**
 - GitHub Pages não executa back-end.
 - Utilize apenas tecnologias realmente implementadas.

---

##  4.3 Wireframes ou Mockups (A partir da Sprint 2)

Apresente os protótipos das telas (Wireframes/Mockups) apenas das funcionalidades que estão sendo implementadas na Sprint atual.

Cada Wireframe ou Mockups devem estar associados a pelo menos:

- Um Requisito Funcional (RF-XX)
- Uma História de Usuário
  
## 📎 Wireframes/ Mockups do Projeto de Software

### 📌 Tela Inicial

Representação do Wireframe:

<img src="images/HomePage.png" width="80%">

### 📌 Tela de Login (RF-02)

**História associada:** Como usuário, eu quero realizar login com meu e-mail e senha para que eu possa acessar meus registros de humor.

Representação do Wireframe:

<img src="images/Login.png" width="80%">

**Descrição:** Permite que o usuário acesse o sistema por meio do preenchimento dos campos de e-mail e senha, com validação dos dados inseridos e opção de envio das credenciais para autenticação. Após o login bem-sucedido, o usuário é direcionado para a tela inicial. 

### 📌 Tela de Cadastro (RF-01)

**História associada:** Como usuário, eu quero criar uma conta para que eu possa acessar o sistema de forma segura.

**Descrição:** Possibilita ao usuário criar uma nova conta informando nome, e-mail e senha. Após o cadastro realizado com sucesso, o usuário pode acessar o sistema utilizando suas credenciais.

Representação do Wireframe:

<img src="images/Cadastro.png" width="80%">

### 📌 Tela de Registro de Humor Diário (RF-03)

**História associada:** Como usuário, eu quero registrar meu humor diariamente para que eu possar compreender meu estado emocional ao longo do tempo.

Representação do Wireframe:

<img src="images/Registro_Humor.png" width="80%">

**Descrição:** A interface permite registrar o humor diário com validação no backend e persistência dos dados no banco, contemplando o RF-03.

---

🔧 **Ferramenta utilizada:**

- Figma
   
---

## 4.4 Modelagem de Dados (Sprint 2 e 3)

O sistema exige persistência de dados.

A documentação do banco seguirá a abordagem de **entrega contínua**, sendo expandida conforme evolução do projeto.

---

### 4.4.1 Script Físico (Entrega na Sprint 2 - MVP)

Para a primeira fatia vertical (MVP), o Squad deverá entregar o **script de criação das tabelas ou coleções utilizadas**.

#### 🔹 Para Banco Relacional (SQL)

Incluir:

- Comandos `CREATE TABLE`
- Definição de chave primária (PK)
- Definição de chaves estrangeiras (FK)

**Exemplo:**

```sql
CREATE TABLE Usuario (
    Id INT PRIMARY KEY,
    Nome VARCHAR(100),
    Email VARCHAR(150) UNIQUE,
    Senha VARCHAR(200)
);
```

---

### Para Banco NoSQL

Incluir a estrutura dos documentos JSON (Schema).

**Exemplo:**

```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "senha": "hash_da_senha"
}
```

### 📁 Obrigatório

O arquivo .sql ou .js deve ser salvo na pasta: src/bd

 - É permitido colar um trecho do script no README apenas para visualização rápida.
 
---
### 4.4.2 Representação do Modelo Físico de Dados (Entrega na Sprint 3 - Core)


> **Fundamentação:** Os modelos de dados físicos fornecem detalhes minuciosos que auxiliam administradores e desenvolvedores na implementação da lógica de negócios em um banco de dados real.
> Eles incluem elementos não especificados no modelo lógico, como:
> - Tipos de dados específicos da plataforma
> - Restrições
> - Índices
> - Triggers (quando aplicável)
> - Procedimentos armazenados (quando aplicável)
>
>Por representarem um banco real, devem respeitar:
> - Convenções de nomenclatura
> - Restrições da plataforma
> - Uso adequado de palavras reservadas <br>


**Exemplo:**

<img src="https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2021/11/09/BDB-1321-image005.png" width="85%">

**FONTE:** <https://aws.amazon.com/pt/compare/the-difference-between-logical-and-physical-data-model/>

<br>O grupo deverá gerar um diagrama físico do banco de dados (estrutura real das tabelas), evidenciando PKs, FKs e relacionamentos, conforme implementado no código.

Este modelo deve exibir:
- Tabelas ou coleções existentes
- Atributos com seus respectivos tipos de dados
- Chaves Primárias (PK)
- Chaves Estrangeiras (FK)
- Relacionamentos entre tabelas
- Restrições implementadas (quando aplicável)

---

### 📌 Requisitos Obrigatórios

- O diagrama deve representar fielmente o banco já implementado.
- Deve refletir exatamente o que foi criado nas Sprints 2 e 3.
- Não incluir tabelas que não existam no código.
- Deve contemplar o controle de acesso de usuários, quando implementado.
- Deve respeitar as convenções e restrições da plataforma utilizada.

---

### 📎 Representação do Modelo Físico de Dados
🚨 O grupo deverá inserir aqui a imagem do diagrama físico de dados.

---
🔧**Ferramentas Sugeridas**
- MySQL Workbench (engenharia reversa automática)
- DbDesigner
- Lucidchart
