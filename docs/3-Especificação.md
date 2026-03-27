# 3. Especificações do Projeto

📌 **Pré-requisito:** Planejamento do Projeto (Cronograma e Sprints definidos).

Nesta seção serão detalhados:

- ✅ Requisitos Funcionais  
- ✅ Histórias de Usuário  
- ✅ Requisitos Não Funcionais  
- ✅ Restrições do Projeto  

**Objetivo**: organizar claramente as funcionalidades, qualidades e limites da solução.

---

# 3.1 Requisitos Funcionais

Os **Requisitos Funcionais (RF)** descrevem o que o sistema deve fazer.

📌 Cada requisito deve:

- Representar uma funcionalidade única
- Ser claro e objetivo
- Orientar diretamente o desenvolvimento

---


## Tabela de Requisitos Funcionais

| ID    | Descrição do Requisito | Prioridade | 
|-------|------------------------|------------| 
| RF-01 | O sistema deve permitir que usuários realizem cadastro informando nome, e-mail e senha. | 🔴 ALTA | 
| RF-02 | O sistema deve permitir que usuários realizem login com credenciais válidas. | 🔴 ALTA | 
| RF-03 | O sistema deve permitir que o usuário registre seu humor diário. | 🔴 ALTA | 
| RF-04 | O sistema deve permitir que o usuário adicione observações ao registro de humor. | 🟡 MÉDIA | 
| RF-05 | O sistema deve permitir que o usuário exclua seus registros. | 🟡 MÉDIA |
| RF-06 | O sistema deve permitir a visualização do histórico de registros emocionais. | 🔴 ALTA |
| RF-07 | O sistema deve permitir filtrar registros por data ou período. | 🟡 MÉDIA | 
| RF-08 | O sistema deve apresentar um dashboard com análise de humor. | 🔴 ALTA | 
| RF-09 | O sistema deve permitir que o usuário visualize gráficos de frequência dos tipos de humor. | 🔴 ALTA | 
| RF-10 | O sistema deve permitir que o usuário visualize padrões emocionais ao longo do tempo. | 🟡 MÉDIA | 

---

# 3.2 Histórias de Usuário

Cada história deve seguir o padrão ensinado na disciplina:

> **Como** [persona],  
> **eu quero** [funcionalidade],  
> **para que** [benefício].

Cada História de Usuário deve estar associada a um Requisito Funcional específico (RF-XX).

## Histórias do Projeto

---

### MÓDULO: Cadastro e Autenticação

### História 1 (relacionada ao RF-01)

Como usuário

Eu quero criar uma conta 

Para que eu possa acessar o sistema de forma segura


### História 2 (relacionada ao RF-02)

Como usuário

Eu quero realizar login com meu e-mail e senha

Para que eu possa acessar meus registros de humor

---

### MÓDULO: Registro de Humor

### História 3 (relacionada ao RF-03)

Como usuário

Eu quero registrar meu humor diariamente

Para que eu possar compreender meu estado emocional ao longo do tempo


### História 4 (relacionada ao RF-04)

Como usuário

Eu quero adicionar observações aos meus registros

Para que eu possa detalhar melhor como foi meu dia


### História 5 (relacionada ao RF-05)

Como usuário

Eu quero excluir meus registros de humor

Para que eu possa remover informações indesejadas

---

### MÓDULO: Histórico de Registros

### História 6 (relacionada ao RF-06)

Como usuário

Eu quero visualizar meu histórico de registros emocionais

Para que eu possa analisar ao longo do tempo


### História 7 (relacionada ao RF-07)

Como usuário

Eu quero filtrar meus registros por data ou período

Para que eu encontre informações específicas com facilidade


### MÓDULO: Dashboard e Análise

### História 8 (relacionada ao RF-08)

Como usuário

Eu quero visualizar um dashboard com análise do meu humor

Para que eu entenda melhor meu comportamento emocional


### História 9 (relacionada ao RF-09)

Como usuário

Eu quero visualizar gráficos de frequência 

Para que eu identifique quais emoções são mais recorrentes


### História 10 (relacionada ao RF-10)

Como usuário

Eu quero visualizar padrões emocionais

Para que eu identifique tendências no meu comportamento 

---

# 3.3 Requisitos Não Funcionais

Os **Requisitos Não Funcionais (RNF)** definem características de qualidade do sistema, como:

- ⚡ Desempenho  
- 🔒 Segurança  
- 🎨 Usabilidade  
- 📈 Escalabilidade  
- 🌐 Compatibilidade  

Eles garantem a qualidade da solução.

---

## Tabela de Requisitos Não Funcionais

| ID     | Descrição do Requisito | Prioridade |
|--------|------------------------|------------|
| RNF-01 | O sistema deve processar requisições do usuário em no máximo 3s. | 🟡 MÉDIA |
| RNF-02 | O sistema deve possuir interface intuitiva e amigável. | 🔴 ALTA |
| RNF-03 | O sistema deve ser responsivo para dispositivos móveis e desktops. | 🔴 ALTA |
| RNF-04 | O sistema deve garantir persistência e integridade dos dados armazenados no banco de dados. | 🔴 ALTA |
| RNF-05 | O sistema deve implementar autenticação segura de usuários para validação de credenciais. | 🔴 ALTA |
| RNF-06 | O sistema deve garantir segurança e privacidade dos dados dos usuários por meio de controle de acesso. | 🔴 ALTA |

---

# 3.4 Restrições do Projeto

📌 **Restrições** são limitações externas impostas ao projeto.

Elas podem envolver:

- 📅 Prazo
- 🖥️ Tecnologia obrigatória ou proibida
- 🌐 Ambiente de execução
- 📜 Normas legais
- 🏢 Políticas institucionais

⚠️ Diferente dos RNFs, as restrições impõem **limites fixos** ao projeto.

---

## Tabela de Restrições

| ID  | Restrição |
|-----|-----------|
|R-01| O projeto deve ser desenvolvido até o final do semestre. |
|R-02| O sistema dev ser desenvolvido como aplicação web. |
|R-03| O sistema deve utilizar banco de dados relacional definido pela equipe. |
|R-04| O sistema deve utilizar tecnologias web definidas pela equipe. |
|R-05| O desenvolvimento do projeto deve respeitar os prazos estabelecidos para cada etapa.	|
|R-06| O sistema deve passar por testes de validação antes de cada entrega parcial. |
|R-07| O projeto deve ser revisado pela equipe antes da entrega final. |

---

## 3.5 Regras de Negócio

> Regras de Negócio definem as condições e políticas que o sistema deve seguir para garantir o correto funcionamento alinhado ao negócio.  
>  
> Elas indicam **quando** e **como** certas ações devem ocorrer, usando o padrão:  
>  
> **Se (condição) for verdadeira, então (ação) deve ser tomada.**  
>  

---

A tabela abaixo deve ser preenchida com as regras de negócio que **impactam seu projeto**. 

|  ID   | Regra de Negócio                                                      |
|-------|-----------------------------------------------------------------------|
| RN-01 | Se um usuário não estiver autenticado, então o acesso às funcionalidades deve ser bloqueado. |                 
| RN-02 |	Se um usuário tentar acessar dados de outro usuário, então o acesso deve ser negado. | 
| RN-03 |	Se os campos obrigatórios não forem preenchidos corretamente, então o cadastro não deve ser concluído. | 
| RN-04 |	Se as credenciais informadas forem inválidas, então o login deve ser negado. | 
| RN-05 |	Se um usuário não selecionar um humor, então o registro não deve ser salvo. | 
| RN-06 |	Se um usuário não adicionar observações, então o registro poderá ser salvo normalmente. | 
| RN-07 |	Se não houver registros cadastrados, então o sistema deve informar que não há dados disponíveis. | 
| RN-08 |	Se um usuário acessar o dashboard, então apenas seus dados devem ser exibidos. | 
| RN-09 |	Se um usuário aplicar filtros de data, então apenas os registros do período selecionado devem ser exibidos. | 
| RN-10 |	Se um usuário desejar editar seus dados, então ele deve estar autenticado. | 
| RN-11 |	Se os dados do usuário forem armazenados, então devem ser protegidos e não compartilhados sem autorização. | 

---
