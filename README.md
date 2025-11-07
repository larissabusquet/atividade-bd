# Sistema de Gerenciamento de Biblioteca - SQLite e Python.

## Parte 1: Explicando o código.

### **Como executar o projeto?**

#### 1. Clone o repositório 
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio 

##### 2. Crie e ative o ambiente virtual

**Linux/Mac**:
```bash 
python3 -m venv venv
source venv/bin/activate 
```

**Windows**:
```bash 
python -m venv venv
venv\Scripts\activate 
```
#### 3. Instale dependências
```bash 
pip install -r requirements.txt 
```
**Nota:** SQLite3 já vem instalado com Python

#### 4. Execute o script 
```bash 
python livros_sqlite.py 
```
#### Funcionalidades implementadas 

- Criação de tabelas com constraints
- Inserção de múltiplos registros 
- Consultas com filtros (WHERE)
- Atualização dos registros (UPDATE)
- Ordenação dos resultados (ORDER BY)
- Exclusão dos registros (DELETE)
- Alteração da estrutura da tabela (ALTER TABLE)
- Remoção de tabelas (DROP TABLE)

#### **Estrutura da tabela**:

## Tabela: Livros

| Campo | Tipo | Restrições |
|-------|------|------------|
| id | ``INTEGER`` | PRIMARY KEY, AUTOINCREMENT |
| titulo | ``TEXT`` | NOT NULL, UNIQUE |
| autor | ``TEXT`` | - |
| ano | ``INTEGER`` | - |
| genero | ``TEXT`` | - |
| disponivel | ``INTEGER`` | DEFAULT 1 (1=disponível, 0=indisponível) |

## Tabela: Usuario (removida no final)

| Campo | Tipo | Restrições |
|-------|------|------------|
| id | ``INTEGER`` | PRIMARY KEY, AUTOINCREMENT |
| nome | ``TEXT`` | - |
| idade | ``INTEGER`` | Adicionada por ALTER TABLE |

--

## Parte 2: Questões Teóricas

### Fundamentos de Bancos de Dados

#### 1. Por que os bancos de dados são essenciais em aplicações modernas?

Os bancos de dados são essenciais porque permitem o armazenamento organizado, seguro e eficiente de grandes volumes de informações. Eles garantem persistência dos dados (mesmo depois do sistema ser desligado), permitem o acesso simultâneo de vários usuários, oferecem funcionalidades de backup e recuperação, e possibilitam consultas complexas de forma rápida.

**Fonte:** https://www.oracle.com/database/what-is-database/

#### 2. Quais são as duas principais categorias de bancos de dados existentes?

- **Bancos de Dados Relacionais (SQL)**: Organizam dados em tabelas com linhas e colunas, utilizando relacionamentos entre elas. 

- **Bancos de Dados Não Relacionais (NoSQL)**: Armazenam dados em formatos flexíveis como documentos, chave-valor, grafos ou colunas. 

**Fonte:** https://www.ibm.com/cloud/blog/sql-vs-nosql

#### 3. Em quais cenários é recomendado utilizar um banco de dados relacional?

Bancos de dados relacionais são ideais para:

- Aplicações que exigem transações ACID (sistemas bancários, e-commerce)
- Dados estruturados com relacionamentos claros
- Necessidade de consultas complexas com JOINs
- Integridade referencial crítica
- Aplicações com schema bem definido e estável
- Relatórios e análises complexas

**Fonte:** https://aws.amazon.com/relational-database/

#### 4. De que forma os recursos de hardware (CPU, memória, disco) afetam a performance de um banco de dados?

- **CPU**: Processa queries complexas, cálculos e ordenações. Mais núcleos permitem processamento paralelo de múltiplas consultas.
- **Memória RAM**: Armazena cache e dados frequentemente acessados, reduzindo acessos ao disco (muito mais lentos).
- **Disco**: SSDs são significativamente mais rápidos que HDDs para operações de I/O. A velocidade de leitura/gravação impacta diretamente o desempenho.
- **Rede**: Em sistemas distribuídos, a latência de rede afeta a comunicação entre nós.

**Fonte:** https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-monitoring-and-tuning-tools

#### 5. O que significa escalabilidade no contexto de bancos de dados?

Escalabilidade é a capacidade de um sistema lidar com crescimento de carga de trabalho. Existem dois tipos:

- **Escalabilidade Vertical (Scale-Up)**: Aumentar recursos do servidor existente (mais CPU, RAM, disco). Limitada pelo hardware disponível.
- **Escalabilidade Horizontal (Scale-Out)**: Adicionar mais servidores ao sistema. Mais complexo, mas permite crescimento ilimitado.

**Fonte:** (https://www.mongodb.com/basics/scaling)

#### 6. Qual a relevância de organizar corretamente os dados em bancos relacionais?

A organização correta (normalização) evita:

- **Redundância**: Dados duplicados ocupam espaço desnecessário
- **Anomalias**: Inconsistências ao inserir, atualizar ou deletar dados
- **Desperdício de recursos**: Queries menos eficientes
- **Dificuldade de manutenção**: Alterações complexas e propensas a erros

A normalização garante integridade, eficiência e facilita a manutenção do banco de dados.

**Fonte:** (https://www.geeksforgeeks.org/introduction-of-database-normalization/)

#### 7. Como escolher entre SQL e NoSQL para um novo projeto?

**Escolher SQL quando:**

- Dados estruturados com relacionamentos complexos
- Necessita de transações ACID
- Schema é estável e bem definido
- Queries complexas com JOINs são frequentes

**Escolher NoSQL quando:**

- Dados não estruturados ou semi-estruturados
- Necessita de alta escalabilidade horizontal
- Schema flexível que muda frequentemente
- Foco em performance de leitura/escrita massiva
- Dados hierárquicos ou em grafo

**Fonte:** (https://www.digitalocean.com/community/tutorials/sql-vs-nosql-choosing-a-database)

---

### Comandos SQL

#### 1. Qual é a finalidade do comando SELECT em SQL?

O comando SELECT é usado para consultar e recuperar dados de uma ou mais tabelas. Ele permite especificar quais colunas retornar, aplicar filtros (WHERE), ordenar resultados (ORDER BY), agrupar dados (GROUP BY) e limitar quantidade de registros (LIMIT).

**Fonte:** [W3Schools - SQL SELECT](https://www.w3schools.com/sql/sql_select.asp)

#### 2. O que significam as siglas DML e DDL em bancos de dados?

- **DML (Data Manipulation Language)**: Comandos para manipular dados dentro das tabelas. Exemplos: SELECT, INSERT, UPDATE, DELETE
- **DDL (Data Definition Language)**: Comandos para definir e modificar a estrutura do banco de dados. Exemplos: CREATE, ALTER, DROP, TRUNCATE

**Fonte:** (https://www.javatpoint.com/dbms-sql-command)

#### 3. Para que serve a cláusula WHERE em consultas SQL?

A cláusula WHERE filtra os registros baseado em condições específicas. Ela determina quais linhas vão ser retornadas, atualizadas ou deletadas. Pode usar operadores de comparação, lógicos e especiais.

**Fonte:** (https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-where/)

#### 4. Por que é fundamental estabelecer uma chave primária (PRIMARY KEY) em tabelas?

A chave primária:

- Identifica unicamente cada registro na tabela
- Garante integridade impedindo duplicatas
- Melhora performance pois é automaticamente indexada
- Permite relacionamentos com outras tabelas (chave estrangeira)
- Facilita atualizações e exclusões específicas

**Fonte:** (https://www.sqlshack.com/sql-primary-key/)

#### 5. Como funciona o comando UPDATE e qual sua sintaxe básica?

O UPDATE modifica dados existentes em uma tabela. É muito importante usar WHERE para especificar quais registros atualizar, caso contrário TODOS os registros serão alterados.

**Fonte:** (https://www.mysqltutorial.org/mysql-basics/mysql-update/)

#### 6. Qual a função do comando DELETE em SQL?

DELETE remove os registros de uma tabela baseado em uma condição WHERE. Ele apenas remove dados, mantendo a estrutura intacta.

**Diferenças:**

- **DELETE**: Remove linhas, mantém estrutura
- **DROP**: Remove tabela completamente
- **TRUNCATE**: Remove todas as linhas rapidamente, mantém estrutura

**Fonte:** (https://www.tutorialspoint.com/sql/sql-delete-query.htm)

#### 7. Como a cláusula ORDER BY organiza os resultados de uma consulta?

ORDER BY ordena os resultados baseado em uma ou mais colunas.

- **ASC (Ascending)**: Ordem crescente (padrão)
- **DESC (Descending)**: Ordem decrescente

**Fonte:** (https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SELECT.html)

#### 8. Para que serve o comando LIMIT em consultas SQL?

LIMIT restringe o número de registros retornados por uma consulta. 

**Fonte:** (https://www.sqlitetutorial.net/sqlite-limit/)

---

### Outros Conceitos

#### 1. Por que é importante integrar o banco de dados com a camada de back-end da aplicação?

A integração é fundamental porque:

- **Separação de responsabilidades**: Lógica de negócio no back-end, dados no BD
- **Segurança**: Back-end valida e sanitiza dados antes de consultar o BD
- **Abstração**: Front-end não acessa BD diretamente, reduzindo vulnerabilidades
- **Escalabilidade**: Facilita otimizações e mudanças sem afetar outras camadas
- **Reutilização**: APIs podem servir múltiplos clientes (web, mobile, desktop)

**Fonte:** (https://www.freecodecamp.org/news/backend-development-best-practices/)

#### 2. O que são views (visões) em bancos de dados e quais suas vantagens?

Views são tabelas virtuais baseadas em consultas SQL. Elas não armazenam dados fisicamente, mas apresentam dados de uma ou mais tabelas.

**Vantagens:**

- Simplificação de consultas complexas
- Segurança: expõem apenas colunas específicas
- Consistência na lógica de negócio
- Abstração da estrutura das tabelas

**Fonte:** (https://www.postgresql.org/docs/current/sql-createview.html)

#### 3. Quais são as propriedades ACID e por que são cruciais para transações?

ACID garante confiabilidade em transações:

- **Atomicidade**: Se uma parte falha, tudo é revertido.
- **Consistência**: Dados sempre passam de um estado válido para outro.
- **Isolamento**: Transações concorrentes não interferem entre si.
- **Durabilidade**: Transação confirmada persiste mesmo com falhas do sistema.

São cruciais em sistemas financeiros, e-commerce e qualquer aplicação onde integridade de dados é crítica.

**Fonte:** (https://database.guide/what-are-acid-properties-in-a-database/)

#### 4. O que estabelece o Princípio do Privilégio Mínimo em segurança de bancos de dados?

O Princípio do Privilégio Mínimo determina que usuários e aplicações devem ter apenas as permissões mínimas necessárias para realizar suas funções. Isso reduz riscos de acesso não autorizado, modificações acidentais e danos causados por contas comprometidas.

**Fonte:** (https://owasp.org/www-community/Access_Control)

---
