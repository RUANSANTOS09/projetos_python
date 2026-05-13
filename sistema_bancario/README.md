# 🏦 Banco Python

> Sistema bancário simples desenvolvido em Python, demonstrando conceitos fundamentais da linguagem na prática.

---

## 📋 Sobre o Projeto

O **Banco Python** é um mini sistema bancário de linha de comando que simula operações bancárias básicas. O projeto foi desenvolvido com foco em consolidar e aplicar conceitos essenciais do Python, transformando lógica de programação em uma solução funcional e interativa.

---

## ✨ Funcionalidades

| Operação | Descrição |
|----------|-----------|
| 💰 Depósito | Adiciona valor ao saldo atual e registra no histórico |
| 💸 Saque | Subtrai valor do saldo atual e registra no histórico |
| 📄 Extrato | Exibe o resumo de todas as movimentações realizadas |
| 🚪 Sair | Encerra a aplicação |

---

## 🧠 Conceitos Aplicados

Este projeto foi construído com os conceitos que domino em Python:

- **Variáveis e tipos de dados** — uso de `float` para valores monetários e `int` para contadores de transações
- **Entrada e saída de dados** — captura de informações do usuário com `input()` e exibição com `print()`
- **Formatação de strings** — uso do método `.format()` e *f-strings* para exibir valores monetários formatados (ex: `R$ 150.00`) e criar separadores visuais dinâmicos com alinhamento (`{:=>26}`)
- **Operadores aritméticos** — manipulação de saldo com `+=` e `-=`
- **Estruturas condicionais** — tomada de decisão com `if`, `elif` e `else` para tratar cada operação do menu
- **Laço de repetição `while True`** — manutenção do menu ativo até que o usuário escolha sair
- **Controle de fluxo** — uso de `break` para encerrar o loop corretamente

---

## 🚀 Como Executar

**Pré-requisito:** Python 3.x instalado.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/banco-python.git

# Acesse a pasta do projeto
cd banco-python

# Execute o programa
python banco.py
```

---

## 🖥️ Demonstração

```
===== Banco Python =====
Saldo atual: R$ 1000.00

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
Escolha: 1

======== DEPOSITO ========
Valor do deposito: R$ 500.00
Deposito realizado! Saldo: R$ 1500.00
==========================

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
Escolha: 3

======== Extrato ========
Saque realizado! - R$ 0.00
Deposito realizado! + R$ 500.00
--------------------------
Total de transações: 1
Saldo atual: R$ 1500.00
==========================
```

---

## 📁 Estrutura do Projeto

```
banco-python/
└── banco.py       # Arquivo principal com toda a lógica do sistema
```

---

## 🔮 Possíveis Melhorias Futuras

- [ ] Validação para impedir saque maior que o saldo disponível
- [ ] Limite diário de saques
- [ ] Histórico detalhado com data e hora de cada transação
- [ ] Suporte a múltiplos usuários
- [ ] Persistência de dados em arquivo `.json` ou banco de dados

---

## 👨‍💻 Autor

Desenvolvido como projeto de prática para consolidar os fundamentos de Python.

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.