# 🧹 Validador de Cadastro de Clientes — Limpeza e Validação de Dados

> Script Python que limpa e valida dados cadastrais de clientes, normalizando nomes e verificando a integridade de endereços de e-mail antes de classificá-los como válidos ou inválidos.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Tema](https://img.shields.io/badge/Tema-Data%20Cleaning-D4A574?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este script resolve um problema extremamente comum em pipelines de dados reais: **dados de cadastro chegam sujos**. Nomes com espaços extras e capitalização inconsistente, e-mails sem formatação válida — tudo isso precisa ser **limpo e validado** antes de seguir para qualquer etapa de análise ou armazenamento.

Diferente dos dois projetos anteriores (que processavam arquivos de texto linha a linha), este trabalha com **dados estruturados em memória** (lista de tuplas), simulando o formato em que dados costumam chegar de uma API ou de uma consulta a banco de dados.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Desempacotamento de tuplas** | `for nome, email in clientes:` — acesso direto aos dois campos de cada registro |
| **Manipulação de strings encadeada** | `.strip().title()` — limpeza e formatação em uma única expressão |
| **Validação com operadores lógicos** | `'@' in email and '.' in email` — verificação de integridade sem uso de regex |
| **Estrutura condicional `if/else`** | Classificação binária de cada registro, sem condições redundantes |
| **Gerenciamento de contexto (`with`)** | Escrita dos dois relatórios finais (válidos e inválidos) |

---

## 🏗️ Fluxo do processamento

```
┌────────────────────────────┐
│   Lista de tuplas (nome,     │
│        email) em memória      │
└──────────────┬───────────────┘
               │ for nome, email in clientes:
               ▼
       ┌───────┴────────┐
       │  Limpeza:        │
       │  .strip().title() │
       └───────┬────────┘
               ▼
       ┌───────┴────────┐
       │  Validação:      │
       │ '@' e '.' no email│
       └───┬────────┬─────┘
           ▼        ▼
     ┌─────────┐ ┌──────────┐
     │ VÁLIDO   │ │ INVÁLIDO  │
     └────┬────┘ └─────┬────┘
          ▼            ▼
  ┌────────────┐ ┌──────────────┐
  │customer_v   │ │ customer_i    │
  │   .txt        │ │   .txt          │
  └────────────────┘ └────────────────┘
```

---

## 💻 Exemplo de uso

```python
clientes = [
    ('  Ana Silva ', 'ana.silva@email.com'),
    ('BRUNO COSTA', 'brunocostaemail.com'),
]

# Saída em customer_v.txt:
# Ana Silva - ana.silva@email.com

# Saída em customer_i.txt:
# Bruno Costa - brunocostaemail.com

# Console:
# Total de clientes válidos: 1
# Total de clientes inválidos: 1
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
├── main.py              # Código-fonte do projeto
├── customer_v.txt          # Relatório de cadastros válidos
├── customer_i.txt          # Relatório de cadastros inválidos
└── README.md
```

---

## 🚀 Próximos passos

- [ ] Validar e-mail com expressão regular (`re`) para maior precisão
- [ ] Adicionar validação de telefone como segundo critério
- [ ] Detectar e remover registros duplicados antes da validação

---

## 🛠️ Tecnologias

- **Python 3** — sem bibliotecas externas

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **Python e Engenharia de Dados**.

<p align="center">
  <i>Mini projeto 3 de uma série prática rumo à Engenharia de Dados. 🛤️</i>
</p>