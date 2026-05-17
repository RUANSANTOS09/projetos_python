# Lojinha Python

> Terminal-based shopping system built to validate core programming fundamentals.

---

## About

Lojinha Python is a command-line shopping simulation built entirely in Python. The project was created as a practical checkpoint — instead of solving isolated exercises, the goal was to build something complete and functional that naturally demanded every concept studied up to this point.

No libraries. No frameworks. Just raw Python logic.

---

## Motivation

After studying the first programming fundamentals — primitive types, relational and logical operators, conditionals, and loops — the challenge was to prove those concepts were actually understood, not just memorized.

Building a real (mini) system forced every concept to be applied with purpose:

- A balance that updates on every transaction isn't a variable exercise — it's state management.
- A menu that stays open until the user decides to leave isn't a loop exercise — it's control flow.
- Blocking a purchase when funds are insufficient isn't a conditional exercise — it's business logic.

The code is simple. The thinking behind it isn't.

---

## Features

- Browse products across 4 store sections
- Real-time balance validation before every purchase
- Product return system with automatic balance update
- Transaction summary with total spent, total refunded, and transaction count
- Nested navigation menus with `while` loops

---

## Store Sections

| Section | Products |
|---|---|
| 🧊 Frios | Peixe Tilápia, Coxinha Congelada, Pizza Frango com Catupiry |
| 🥦 Verduras | Tomate, Cenoura, Cebola |
| 🍎 Frutas | Banana Prata, Laranja Pêra, Maçã Nacional |
| 🧴 Limpeza | Detergente, Sabão em Pó, Amaciante de Roupas |

---

## Concepts Applied

| Concept | Application |
|---|---|
| Primitive types | Balance and prices as `float`, menu options as `int` |
| Relational operators | Balance check before each purchase (`<=`) |
| Logical operators | Compound condition validation |
| `if / elif / else` | Menu navigation and purchase decisions |
| `while` | Persistent menus, nested section loops |

---

## Getting Started

**Requirements:** Python 3.x

```bash
# Clone the repository
git clone https://github.com/your-username/lojinha-python.git

# Navigate to the project folder
cd lojinha-python

# Run
python lojinha.py
```

---

## Usage

```
Digite seu saldo atual: R$ 100.00

===== Lojinha Python =====
[1] Comprar
[2] Devolver
[3] Resumo
[4] Sair
Digite um número:
```

Navigate through sections, pick products, and the system handles the rest — balance deduction, validation, and transaction tracking.

---

## Project Structure

```
lojinha-python/
│
├── lojinha.py      # Main application
└── README.md       # Project documentation
```

---

## Roadmap

Features intentionally left out — to be added as new concepts are learned:

- [ ] Product catalog using lists and dictionaries
- [ ] Reusable `purchase(product, price)` function to eliminate code repetition
- [ ] Itemized transaction history (currently only totals are tracked)
- [ ] Data persistence between sessions

---

## Author

Made by **[your name]** — currently learning Python from the ground up.

[![GitHub](https://img.shields.io/badge/GitHub-your--username-181717?style=flat&logo=github)](https://github.com/your-username)