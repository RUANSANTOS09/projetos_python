# 🍽️ Caixa do Restaurante

Projeto desenvolvido durante o aprendizado de Python, com o objetivo de praticar conceitos fundamentais da linguagem em um contexto do cotidiano.

## 📋 Sobre o projeto

O programa simula o caixa de um restaurante simples. Ele recebe o nome do cliente, o prato escolhido e a forma de pagamento, verifica se o cliente é sócio para aplicar desconto, calcula o total e informa se o cliente ganhou uma sobremesa grátis.

## 🧠 Conceitos praticados

- **Variáveis e tipos primitivos** — uso de `str`, `int`, `float` e `bool`
- **Operadores racionais** — comparação de preço para liberar o brinde (`>`)
- **Operadores lógicos** — verificação combinada de forma de pagamento e valor total (`and`)
- **Concatenação** — montagem das mensagens de saída com `.format()`
- **Entrada de dados** — uso de `input()` com `.lower()` e `.upper()` para normalizar respostas
- **if / elif / else** — controle de fluxo para pedidos, desconto de sócio e sobremesa

## 💻 Como executar

Você precisa ter o [Python 3](https://www.python.org/downloads/) instalado.

```bash
python caixa.py
```

## 🍕 Cardápio

| Prato      | Preço    |
|------------|----------|
| Pizza      | R$35,00  |
| X-Burguer  | R$18,00  |
| Suco       | R$8,00   |

## 🎟️ Regras

- **Desconto de sócio:** 15% sobre o valor do pedido
- **Sobremesa grátis:** pagamento em dinheiro com total acima de R$30,00

## 📄 Exemplo de saída

```
Qual o seu nome: João
Escolha seu prato (X-Burguer / Pizza / Suco): Pizza
É sócio do restaurante? (s/n): s
Forma de pagamento - Cartão (1) | Dinheiro (2): 2

----------------------------------------
Olá, João! Você pediu pizza -- R$35.00
Valor original: R$35.00
Desconto de sócio (15%): R$5.25
Total a pagar: R$29.75
Sobremesa grátis? False
----------------------------------------
```

---

Projeto feito com Python 3 como parte dos estudos iniciais da linguagem.