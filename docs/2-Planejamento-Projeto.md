# 2. Planejamento do Projeto

Organização do trabalho ao longo do semestre.  
O projeto adota uma metodologia ágil, simulando o ambiente de uma Software House.

---

✔️ Funcionalidade completa:  

**Banco de Dados → API → Tela**

---

# 2.1 Sprints do Projeto

Projeto realizado em **4 Sprints**, com entregas contínuas de código e documentação.

---

## 📅 Visão Geral

### 🟢 Sprint 1 – Setup, Hello World e Visão do Produto
- README com descrição do projeto
- ODS escolhida
- Backlog macro
- Repositório criado
- Banco de dados instanciado (vazio)
- Tela "Hello World" conectada à API

---

### 🟡 Sprint 2 – MVP (Primeira Fatia Vertical)
- Requisitos Funcionais documentados
- Script do Banco de Dados
- 1ª funcionalidade completa funcionando
- Dados sendo salvos no banco

---

### 🔵 Sprint 3 – Core e Regras de Negócio
- Implementação das regras de negócio
- Validações no backend
- DER atualizado via Engenharia Reversa
- Diagrama de Classes atualizado

---

### 🔴 Sprint 4 – Finalização e Deploy
- Correção de bugs
- Testes finais ponta a ponta
- Documentação final consolidada
- Relatório preenchido no APC
- Sistema pronto para Arguição

---

# 👥 Papéis de Gestão

Organização do time.

- 👨‍💻 **Tech Lead (Git Master)**  
  Responsável pelo repositório e merges.

- 🗄️ **Arquiteto de Dados (DBA Guard)**  
  Responsável pela modelagem e padronização do banco.

- 🧪 **Gerente de Qualidade (QA & Code Reviewer)**  
  Responsável por revisar código e validar testes.

- 📋 **Facilitador Ágil (PO / Scrum Master)**  
  Responsável por prazos, Kanban e priorização do backlog.

---

##  Definição dos Papéis – Sprint 1

- 👨‍💻 Tech Lead: Fredson Marinho Almeida Borges
- 🗄️ Arquiteto de Dados: Fancisco Henrique de Moura
- 🧪 Gerente de Qualidade: Diego Rodrigues da Cruz
- 📋 Facilitador Ágil: Camila Machado Pires Maia

---

# 2.2 Execução e Controle

## 🗂️ Kanban 

### Estrutura do Board:

- A Fazer
- Desenvolver
- Fila para Teste
- Teste
- Feito

### Regras

- Cada cartão deve representar uma Fatia Vertical.
- Todo cartão deve conter:
  - Responsável
  - Descrição
  - Prazo
- A avaliação individual considerará:
  - Histórico de commits
  - Movimentação no Kanban

---

# 📋 Acompanhamento das Sprints

## Legenda de Status

- [x] ✔️ Concluído
- [ ] 📝 Em andamento
- [ ] ⌛ Atrasado
- [ ] ❌ Não iniciado

---

# 🟢 Sprint 1 – Setup

| Responsável                    | Papel                | Tarefa                                                      | Início | Prazo | Status |
|--------------------------------|----------------------|-------------------------------------------------------------|--------|-------|--------|
| Camila Machado Pires Maia      | Facilitador Ágil     | Criar repositório, desenvolver tela de "Login" e formatação | 26/02  | 12/03 | ✔️ |
| Diego Rodrigues da Cruz        | Gerente de Qualidade | Preencher o README.md e Planejamento-Projeto.md             | 26/02  | 12/03 | ✔️ |
| Francisco Henrique de Moura    | Arquiteto de Dados   | Elaborar o Contexto.md e organizar a estrutura de páginas   | 26/02  | 12/03 | ✔️ |
| Fredson Marinho Almeida Borges | Tech Lead            | Criar instância do Banco de Dados                           | 26/02  | 12/03 | ✔️ |

---

# 🟡 Sprint 2 – MVP

| Responsável                    | Papel                | Tarefa                                                                                                                                                  | Início | Prazo | Status |
|--------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------|--------|
| Camila Machado Pires Maia      | Facilitador Ágil     | Documentação Técnica (Especificacao.md), Wireframes e Tela Cadastro (front/back)                                                                        | 19/03  | 06/04 | ✔️    |
| Diego Rodrigues da Cruz        | Gerente de Qualidade | Desenvolvimento da Tela Registro de Humor (Front)                                                                                                       | 19/03  | 06/04 | ✔️    |
| Francisco Henrique de Moura    | Arquiteto de Dados   | Integração do banco de dados PostgreSQL com Django e configuração do ambiente Docker                                                                    | 19/03  | 06/04 | ✔️    |
| Fredson Marinho Almeida Borges | Tech Lead            | Dockerização do PostgreSQL, implementação do backend (Cadastro/Humor) com persistência real e realização de testes de integração e ponta a ponta (E2E)  | 19/03  | 06/04 | ✔️    |

---

# 🔵 Sprint 3 – Core

| Responsável                    | Papel                | Tarefa                                                        | Início | Prazo | Status |
|--------------------------------|----------------------|---------------------------------------------------------------|--------|-------|--------|
| Camila Machado Pires Maia      | Facilitador Ágil     | HomePage funcional, Documentação Técnica completa e Implementação de edição, exclusão e filtro por data | 09/04  | 29/04 | ✔️    |
| Diego Rodrigues da Cruz        | Gerente de Qualidade | Funcionalidade de Editar perfil do usuário (visualizar e editar informações pessoais)                                | 09/04  | 07/05 | ✔️    |
| Francisco Henrique de Moura    | Arquiteto de Dados   | ⁠Emitir alerta ao tentar acessar histórico de registros/Funcionalidade de dashboard  | 09/04  | 29/04 |  ✔️ |
| Fredson Marinho Almeida Borges | Tech Lead            | Atualização de Documentação Técnica (Requisitos, Diagramas) e Criação da Documentação de Engenharia Reversa                               | 09/04  | 07/05 | ✔️    |

---

# 🔴 Sprint 4 – Finalização

| Responsável                    | Papel                | Tarefa | Início | Prazo | Status |
|--------------------------------|----------------------|--------|--------|--------|--------|
| Camila Machado Pires Maia      | Facilitador Ágil     | Documentação Consolidada, Revisões e Formatações finais | 14/05 | 25/06 | ✔️ |
| Diego Rodrigues da Cruz        | Gerente de Qualidade | Documentação do Interface-Sistema e Referências | 14/05 | 25/06 | ✔️ |
| Francisco Henrique de Moura    | Arquiteto de Dados   | Deploy da Aplicação: Disponibilizar o sistema em ambiente acessível (deploy), garantindo que esteja funcional para avaliação , preencher síntese dos resultados, conexão com a ODS, limitações, trabalhos futuros e lições aprendida | 14/05 | 25/06 | ✔️  |
| Fredson Marinho Almeida Borges | Tech Lead            | Testes finais e consolidar README | 14/05 | 25/06 | ✔️ |

---
