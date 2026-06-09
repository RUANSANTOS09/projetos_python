# Cadastro de Fontes de Dados

<p align="center">
  <strong>Mini projeto em Python para praticar listas, funcoes, repositorio em memoria e tratamento de excecoes.</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Status" src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-2E8B57?style=for-the-badge">
  <img alt="Area" src="https://img.shields.io/badge/Area-Engenharia%20de%20Dados-FFB000?style=for-the-badge">
</p>

---

## Visao Geral

O **Cadastro de Fontes de Dados** e um sistema simples executado no terminal que simula uma rotina comum em projetos de dados: registrar, consultar, listar e remover fontes de dados utilizadas por uma empresa.

Mesmo sendo um mini projeto, ele trabalha conceitos importantes para quem esta iniciando em **engenharia de dados**, como organizacao de dados em uma estrutura de armazenamento, separacao de responsabilidades com funcoes e validacao de entradas do usuario.

Exemplos de fontes que podem ser cadastradas:

- Banco PostgreSQL
- Planilha Excel
- API de Vendas
- Arquivo CSV
- Data Lake
- Bucket S3

---

## Intencao Do Projeto

Este projeto foi criado para transformar conceitos basicos de Python em uma aplicacao pequena, mas com comportamento parecido com sistemas reais.

Em engenharia de dados, e comum trabalhar com varias fontes diferentes: bancos relacionais, arquivos, APIs, planilhas, filas e sistemas externos. Antes de processar dados, muitas vezes e necessario **registrar, controlar e validar quais fontes existem**.

```mermaid
flowchart LR
    A["Fontes de Dados"] --> B["Cadastro no Sistema"]
    B --> C["Repositorio em Memoria"]
    C --> D["Listagem"]
    C --> E["Busca"]
    C --> F["Remocao"]
    D --> G["Controle das Fontes"]
    E --> G
    F --> G
```

---

## Objetivos De Aprendizado

Ao construir este projeto, voce pratica:

- Criacao e manipulacao de listas
- Uso de funcoes para organizar responsabilidades
- Uso de uma lista como repositorio em memoria
- Estrutura de menu com `while True`
- Validacao de entrada do usuario
- Tratamento de excecoes com `try` e `except`
- Controle de fluxo com `if`, `elif` e `else`
- Uso de `if __name__ == '__main__':`

---

## Funcionalidades

O sistema deve permitir que o usuario:

| Opcao | Funcionalidade | Descricao |
|---:|---|---|
| 1 | Cadastrar fonte | Adiciona uma nova fonte de dados ao repositorio |
| 2 | Listar fontes | Exibe todas as fontes cadastradas |
| 3 | Buscar fonte | Verifica se uma fonte existe no repositorio |
| 4 | Remover fonte | Remove uma fonte cadastrada |
| 5 | Sair | Encerra o sistema |

---

## Fluxo Do Programa

```mermaid
flowchart TD
    A["Inicio do Programa"] --> B["Exibir Menu"]
    B --> C["Ler Opcao do Usuario"]
    C --> D{"Opcao valida?"}
    D -- "Nao" --> E["Mostrar erro"]
    E --> B
    D -- "Sim" --> F{"Qual opcao?"}
    F -- "1" --> G["Cadastrar fonte"]
    F -- "2" --> H["Listar fontes"]
    F -- "3" --> I["Buscar fonte"]
    F -- "4" --> J["Remover fonte"]
    F -- "5" --> K["Encerrar sistema"]
    G --> B
    H --> B
    I --> B
    J --> B
```

---

## Arquitetura Simples

O projeto pode ser organizado em pequenas funcoes. Cada funcao tem uma responsabilidade clara.

```mermaid
flowchart TB
    M["Menu Principal"] --> C["cadastrar_fonte"]
    M --> L["listar_fontes"]
    M --> B["buscar_fonte"]
    M --> R["remover_fonte"]
    C --> Repo["repositorio_fontes"]
    L --> Repo
    B --> Repo
    R --> Repo
```

---

## Regras De Negocio

O sistema deve respeitar as seguintes regras:

- Nao cadastrar fonte com nome vazio
- Nao remover uma fonte que nao existe
- Informar quando uma busca nao encontrar resultado
- Informar quando nao houver fontes cadastradas
- Tratar erro quando o usuario digitar texto no lugar da opcao numerica
- Manter o programa rodando ate o usuario escolher sair

---

## Exemplo De Uso No Terminal

```text
===== CADASTRO DE FONTES DE DADOS =====
1 - Cadastrar fonte
2 - Listar fontes
3 - Buscar fonte
4 - Remover fonte
5 - Sair

Digite uma opcao: 1
Digite o nome da fonte de dados: Banco PostgreSQL
Fonte cadastrada com sucesso.

===== CADASTRO DE FONTES DE DADOS =====
1 - Cadastrar fonte
2 - Listar fontes
3 - Buscar fonte
4 - Remover fonte
5 - Sair

Digite uma opcao: 1
Digite o nome da fonte de dados: API de Vendas
Fonte cadastrada com sucesso.

===== CADASTRO DE FONTES DE DADOS =====
1 - Cadastrar fonte
2 - Listar fontes
3 - Buscar fonte
4 - Remover fonte
5 - Sair

Digite uma opcao: 2
Fontes cadastradas:
- Banco PostgreSQL
- API de Vendas
```

---

## Exemplo De Tratamento De Erro

```text
===== CADASTRO DE FONTES DE DADOS =====
1 - Cadastrar fonte
2 - Listar fontes
3 - Buscar fonte
4 - Remover fonte
5 - Sair

Digite uma opcao: abc
Opcao invalida. Digite apenas numeros.
```

```text
Digite o nome da fonte de dados:
Nome da fonte nao pode ser vazio.
```

```text
Digite o nome da fonte que deseja remover: Oracle
Fonte nao encontrada. Nao foi possivel remover.
```

---

## Conceitos De Engenharia De Dados

Embora seja um projeto inicial, ele representa ideias presentes em sistemas maiores:

| Conceito no Projeto | Relacao com Engenharia de Dados |
|---|---|
| Fonte de dados | Origem de informacoes usadas em pipelines |
| Repositorio em lista | Estrutura simples para armazenar metadados |
| Cadastro | Registro de fontes disponiveis |
| Busca | Consulta de metadados |
| Remocao | Controle de fontes desativadas ou processadas |
| Validacao | Garantia minima de qualidade da entrada |

---

## Possivel Evolucao

Depois que a primeira versao estiver funcionando, o projeto pode evoluir para:

- Salvar as fontes em arquivo `.txt`
- Salvar os dados em arquivo `.csv`
- Usar dicionarios para guardar mais informacoes
- Adicionar tipo da fonte, como `Banco`, `API`, `CSV` ou `Excel`
- Adicionar status, como `Ativa` ou `Inativa`
- Integrar com banco de dados
- Criar logs das operacoes realizadas

---

## Checklist Do Projeto

- [ ] Criar lista para armazenar as fontes
- [ ] Criar menu principal
- [ ] Criar funcao para cadastrar fonte
- [ ] Criar funcao para listar fontes
- [ ] Criar funcao para buscar fonte
- [ ] Criar funcao para remover fonte
- [ ] Tratar opcao invalida
- [ ] Validar fonte vazia
- [ ] Usar `if __name__ == '__main__':`
- [ ] Testar o fluxo completo no terminal

---

## Estrutura Sugerida

```text
cadastro-fontes-dados/
|
|-- main.py
|-- README.md
```

---

## Como Executar

No terminal, execute:

```bash
python main.py
```

---

## Autor

Projeto desenvolvido como parte dos estudos de Python com foco em fundamentos para engenharia de dados.

---

<p align="center">
  <strong>Um pequeno projeto, mas com mentalidade de sistema real.</strong>
</p>
