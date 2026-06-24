# 💰 Monitor de Vendas — Separação de Pedidos Confirmados e Cancelados

> Script Python que processa um histórico de vendas, separando pedidos confirmados de cancelados em relatórios distintos, com contagem total de cada categoria.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Tema](https://img.shields.io/badge/Tema-Processamento%20de%20Dados-D4A574?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este script simula um **relatório de fechamento de vendas**, onde pedidos com status diferentes (confirmado ou cancelado) precisam ser separados em arquivos distintos — um padrão recorrente em relatórios financeiros e dashboards operacionais.

O projeto reaproveita a mesma estrutura lógica de leitura, filtragem e geração de relatório do projeto anterior (Organizador de Logs), mas aplicada a um **segundo critério de classificação em paralelo** (confirmadas *e* canceladas), reforçando o padrão em um contexto diferente.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Gerenciamento de contexto (`with`)** | Leitura e escrita de múltiplos arquivos de forma seletivamente automática |
| **Desempacotamento e `enumerate()`** | Numeração de cada venda processada, preservando a posição original |
| **Múltiplos acumuladores** | Contagem independente de vendas confirmadas e canceladas |
| **Listas de resultado em memória** | Separação dos dados processados antes da escrita final |
| **Manipulação de strings** | `.startswith()` para classificar o status de cada venda |

---

## 🏗️ Fluxo do processamento

```
┌──────────────────────┐
│   Lista de vendas      │
│    (em memória)         │
└───────────┬─────────────┘
            │ with open(...) as s:
            ▼
┌──────────────────────┐
│     vendas.txt          │  ← arquivo gerado
└───────────┬─────────────┘
            │ leitura + classificação
            ▼
     ┌──────┴──────┐
     ▼             ▼
┌──────────┐  ┌──────────────┐
│CONFIRMADA│  │  CANCELADA    │
└────┬─────┘  └──────┬───────┘
     ▼               ▼
┌──────────────┐ ┌────────────────┐
│approved_sales │ │cancelled_sales  │
│    .txt        │ │     .txt         │
└────────────────┘ └─────────────────┘
```

---

## 💻 Exemplo de uso

```python
vendas = [
    'CONFIRMADA: Notebook - R$ 2500',
    'CANCELADA: Mouse - R$ 50',
    'CONFIRMADA: Teclado - R$ 120',
]

# Saída em cancelled_sales.txt:
# 2: CANCELADA: Mouse - R$ 50
#
# Vendas canceladas: 1
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
├── main.py                  # Código-fonte do projeto
├── vendas.txt                 # Gerado automaticamente na execução
├── cancelled_sales.txt         # Relatório de cancelamentos
├── approved_sales.txt          # Relatório de confirmações
└── README.md
```

---

## 🚀 Próximos passos

- [ ] Calcular o valor total perdido em vendas canceladas
- [ ] Adicionar categoria "pendente" como terceiro status possível
- [ ] Gerar um resumo consolidado em um único arquivo, além dos relatórios separados

---

## 🛠️ Tecnologias

- **Python 3** — sem bibliotecas externas

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **Python e Engenharia de Dados**.

<p align="center">
  <i>Mini projeto 2 de uma série prática rumo à Engenharia de Dados. 🛤️</i>
</p>