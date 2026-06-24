# 📋 Organizador de Logs — Filtro de Eventos de Erro
 
> Script Python que processa um arquivo de log simulado, separando eventos de erro em um relatório dedicado — um padrão comum em monitoramento de pipelines de dados.
 
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Tema](https://img.shields.io/badge/Tema-Manipulação%20de%20Arquivos-D4A574?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)
 
---
 
## 📖 Sobre o projeto
 
Este script simula um cenário comum em **observabilidade de pipelines de dados**: um sistema gera logs de execução misturando eventos informativos e erros, e é preciso **isolar rapidamente as falhas** em um relatório separado, sem perder a referência da posição original de cada evento.
 
A proposta nasceu como exercício de fixação de **manipulação de arquivos com `with`**, combinando leitura, filtragem com `enumerate()` e geração de relatório — habilidades centrais no dia a dia de quem trabalha com ingestão e monitoramento de dados.
 
---
 
## 🧠 Conceitos aplicados
 
| Conceito | Onde aparece no projeto |
|---|---|
| **Gerenciamento de contexto (`with`)** | Abertura e fechamento automático de arquivos, sem `try/except` manual |
| **Manipulação de strings** | `.startswith()` para identificar o tipo de evento, `.rstrip()` para limpar quebras de linha |
| **`enumerate()`** | Numeração das linhas de erro, preservando a posição original no log |
| **Variável acumuladora** | Contagem total de erros, inicializada fora do laço para não ser resetada |
| **Separação de responsabilidades** | Ler e acumular em memória primeiro, escrever o resultado depois |
 
---
 
## 🏗️ Fluxo do processamento
 
```
┌─────────────────────┐
│   Lista de logs      │
│   (em memória)        │
└──────────┬────────────┘
           │ with open(...) as log:
           ▼
┌─────────────────────┐
│     logs.txt          │  ← arquivo gerado
└──────────┬────────────┘
           │ with open(...) as l:
           ▼
┌─────────────────────┐
│  Filtro: startswith   │
│      ('ERRO:')         │
└──────────┬────────────┘
           │ append() em lista nova
           ▼
┌─────────────────────┐
│     erros.txt          │  ← relatório final
└────────────────────────┘
```
 
---
 
## 💻 Exemplo de uso
 
```python
logs = [
    'INFO: Sistema iniciado',
    'ERRO: Falha ao conectar no banco',
    'INFO: Processando arquivo',
    'ERRO: Timeout na requisição',
]
 
# Saída em erros.txt:
# 2: ERRO: Falha ao conectar no banco
# 4: ERRO: Timeout na requisição
#
# Quantidade de erros: 2
```
 
---
 
## ▶️ Como executar
 
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
python main.py
```
 
**Pré-requisitos:** apenas Python 3.10 ou superior — sem dependências externas.
 
---
 
## 📂 Estrutura do repositório
 
```
.
├── main.py          # Código-fonte do projeto
├── logs.txt          # Gerado automaticamente na execução
├── erros.txt          # Relatório final gerado
└── README.md
```
 
---
 
## 🚀 Próximos passos
 
- [ ] Adicionar timestamp simulado em cada linha de log
- [ ] Classificar erros por severidade (CRÍTICO, AVISO, ERRO)
- [ ] Persistir o relatório em formato `.json` além de `.txt`
---
 
## 🛠️ Tecnologias
 
- **Python 3** — sem bibliotecas externas
---
 
## 👤 Autor
 
Projeto desenvolvido como parte de estudos pessoais em **Python e Engenharia de Dados**.
 
<p align="center">
  <i>Mini projeto 1 de uma série prática rumo à Engenharia de Dados. 🛤️</i>
</p>
