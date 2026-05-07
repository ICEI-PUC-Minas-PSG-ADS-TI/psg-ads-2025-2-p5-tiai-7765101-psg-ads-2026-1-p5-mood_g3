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
| RF-05 | O sistema deve permitir que o usuário exclua seus registros. | 🔴 ALTA |
| RF-06 | O sistema deve permitir a visualização do histórico de registros emocionais. | 🔴 ALTA |
| RF-07 | O sistema deve permitir filtrar registros por data ou período. | 🟡 MÉDIA | 
| RF-08 | O sistema deve exibir um alerta de confirmação antes de permitir a visualização do histórico de registros. | 🟡 MÉDIA |
| RF-09 | O sistema deve permitir que o usuário visualize gráficos de frequência dos tipos de humor registrados. | 🔴 ALTA |
| RF-10 | O sistema deve permitir que o usuário visualize padrões emocionais ao longo do tempo. | 🟡 MÉDIA |
| RF-11 | O sistema deve apresentar um dashboard com análise de humor. | 🔴 ALTA |
| RF-12 | O sistema deve permitir que o usuário edite seus registros de humor. | 🔴 ALTA |
| RF-13 | O sistema deve permitir que o usuário visualize e edite seus dados pessoais. | 🔴 ALTA |

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

Para que eu possa analisar e acompanhar a evolução das minhas emoções


### História 7 (relacionada ao RF-07)

Como usuário

Eu quero filtrar meus registros por data ou período

Para que eu encontre informações específicas com facilidade

### História 8 (relacionada ao RF-08)

Como usuário

Eu quero receber um alerta antes de visualizar meu histórico de registros

Para que eu confirme minha intenção de acesso aos meus dados

---

### MÓDULO: Dashboard e Análise

### História 9 (relacionada ao RF-09)

Como usuário

Eu quero visualizar gráficos de frequência

Para que eu identifique quais emoções são mais recorrentes

### História 10 (relacionada ao RF-10)

Como usuário

Eu quero visualizar padrões emocionais

Para que eu identifique tendências no meu comportamento

### História 11 (relacionada ao RF-11) 

Como usuário 

Eu quero visualizar um dashboard com análise do meu humor 

Para que eu entenda melhor meu comportamento emocional

---

### MÓDULO: Edição 

### História 12 (relacionada ao RF-12) 

Como usuário

Eu quero editar meus registros de humor

Para que eu possa corrigir ou atualizar informações registradas anteriormente

### História 13 (relacionada ao RF-13) 

Como usuário

Eu quero visualizar e editar meus dados pessoais

Para que eu possa manter minhas informações atualizadas no sistema

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
| RNF-05 | O sistema deve garantir autenticação segura dos usuários para proteger contra acessos não autorizados. | 🔴 ALTA |

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
|R-02| O sistema deve ser desenvolvido como aplicação web. |
|R-03| O sistema deve respeitar as diretrizes da LGPD no tratamento de dados dos usuários. |
|R-04| O sistema deve ser desenvolvido sem depender de serviços externos pagos para seu funcionamento. |
|R-05| O sistema deve ser desenvolvido em módulos front-end e back-end. |

---

## 3.5 Regras de Negócio

> Regras de Negócio definem as condições e políticas que o sistema deve seguir para garantir o correto funcionamento alinhado ao negócio.  
>  
> Elas indicam **quando** e **como** certas ações devem ocorrer, usando o padrão:  
>  
> **Se (condição) for verdadeira, então (ação) deve ser tomada.**  
>  

---

A tabela abaixo foi preenchida com as regras de negócio que **impactam o projeto**. 

|  ID   | Regra de Negócio                                                      |
|-------|-----------------------------------------------------------------------|
| RN-01 | Se um usuário não estiver autenticado, então o acesso às funcionalidades deve ser bloqueado. |                 
| RN-02 |	Se os campos obrigatórios não forem preenchidos corretamente, então o cadastro não deve ser concluído. | 
| RN-03 |	Se as credenciais informadas forem inválidas, então o login deve ser negado. | 
| RN-04 |	Se um usuário não selecionar um humor, então o registro não deve ser salvo. | 
| RN-05 |	Se não houver registros cadastrados, então o sistema deve informar que não há dados disponíveis. | 
| RN-06 |	Se um usuário aplicar filtros de data, então apenas os registros do período selecionado devem ser exibidos. | 
| RN-07 |	Se os dados do usuário forem armazenados, então devem ser protegidos e não compartilhados sem autorização. | 
| RN-08 | Se um usuário acessar o dashboard, então apenas seus dados devem ser exibidos. |
| RN-09 | Se um usuário desejar editar seus dados, então ele deve estar autenticado, o que garante segurança nas alterações. |
| RN-10 | Se um usuário tentar acessar seu histórico de registros, então o sistema deve exibir um alerta de confirmação antes de permitir o acesso. |

---

## 3.6 Validações e Cálculos Detalhados (Implementação Técnica)

> Esta seção detalha as validações específicas e cálculos utilizados no código.

### 3.6.1 Validações de Cadastro e Autenticação

| ID | Validação | Critério | Exceção |
|---|---|---|---|
| VAL-01 | Formato de Email | RFC 5322 compliant | ValidationError |
| VAL-02 | Unicidade de Email | Não permitir duplicatas | ValidationError: "Email já existente" |
| VAL-03 | Comprimento de Senha | Mínimo 8 caracteres | ValidationError |
| VAL-04 | Complexidade de Senha | Deve conter letra maiúscula + número | ValidationError |
| VAL-05 | Correspondência de Senhas | Confirmação deve coincidir com original | ValidationError: "Senhas não conferem" |
| VAL-06 | Nome de Usuário | Alfanumérico + underscore (máx 150 chars) | ValidationError |

### 3.6.2 Validações de Registro de Humor

| ID | Validação | Critério | Exceção |
|---|---|---|---|
| VAL-10 | Intensidade | Intervalo obrigatório: 1-10 | ValidationError: "Intensidade deve estar entre 1 e 10" |
| VAL-11 | Emoção | Deve estar em: [MUITO_FELIZ, FELIZ, NEUTRO, TRISTE, MUITO_TRISTE, CANSADO, ANSIOSO, ALIVIADO] | ValidationError: "Emoção inválida" |
| VAL-12 | Autenticação | Apenas usuários logados podem registrar | @login_required → Redirect para /login/ |
| VAL-13 | Limite de Requisições | Não permitir múltiplos registros em menos de 1 minuto | Avisar: "Aguarde antes de criar novo registro" |
| VAL-14 | Notas | Máximo 500 caracteres (opcional) | ValidationError se ultrapassar |
| VAL-15 | Timestamp | Automaticamente capturado como `created_at` | Imutável após criação |

### 3.6.3 Validações de Acesso e Segurança

| ID | Validação | Critério | Exceção |
|---|---|---|---|
| VAL-20 | Isolamento de Dados | Usuário A NÃO pode ver dados do Usuário B | Http404 ou PermissionDenied |
| VAL-21 | Edição | Só proprietário pode editar seu registro | Http404 se user != entry.user |
| VAL-22 | Exclusão | Só proprietário pode deletar seu registro | Http404 + require POST (não GET) |
| VAL-23 | CSRF Protection | Todo formulário POST protegido por token CSRF | Rejeitar sem token válido |
| VAL-24 | Password Hashing | Senhas armazenadas com PBKDF2+SHA256 (padrão Django) | Nunca armazenar em plain text |

### 3.6.4 Cálculos de Métricas e Estatísticas

| ID | Métrica | Fórmula | Tipo | Uso |
|---|---|---|---|---|
| CALC-01 | Intensidade Média Diária | SUM(intensidade) / COUNT(registros) | Decimal | Dashboard diário |
| CALC-02 | Emoção Predominante | MODE(emoção) últimos 30 dias | Categoria | Card no dashboard |
| CALC-03 | Variação (StdDev) | √(Σ(x - μ)² / N) | Decimal | Gráfico de volatilidade |
| CALC-04 | Dias com Registro | COUNT(DISTINCT date(created_at)) | Integer | Estatística de comprometimento |
| CALC-05 | Dias sem Registro | Total dias - Dias com registro | Integer | Identificar gaps |
| CALC-06 | Emoção por Frequência | GROUP BY emotion ORDER BY count DESC | Lista | Gráfico de pizza |

### 3.6.5 Fluxos de Autorização e Acesso

#### Matriz de Controle de Acesso

| Funcionalidade | Anônimo | Usuário Logado | Admin |
|---|---|---|---|
| Ver Home | ✅ | ✅ | ✅ |
| Login | ✅ | ❌ (redir. a dashboard) | ❌ |
| Registrar | ✅ | ❌ (redir. a dashboard) | ✅ |
| Acessar Dashboard | ❌ (redir. a login) | ✅ | ✅ |
| Criar Registro | ❌ (redir. a login) | ✅ (próprio) | ✅ |
| Editar Registro | ❌ (redir. a login) | ✅ (próprio apenas) | ✅ |
| Deletar Registro | ❌ (redir. a login) | ✅ (próprio apenas) | ✅ |
| Ver Histórico | ❌ (redir. a login) | ✅ (próprio) | ✅ |
| Acessar Admin | ❌ | ❌ | ✅ |

---
