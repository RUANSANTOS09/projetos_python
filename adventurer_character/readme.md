# ⚔️ Ficha do Aventureiro

Projeto desenvolvido durante o aprendizado de Python, com o objetivo de praticar conceitos fundamentais da linguagem.

## 📋 Sobre o projeto

O programa monta a ficha de um personagem de RPG e avalia suas condições de batalha: se pode entrar em uma masmorra e se está apto para atacar.

## 🧠 Conceitos praticados

- **Variáveis e tipos primitivos** — uso de `str`, `int` e `bool`
- **Operadores racionais** — comparação de nível com o requisito da masmorra (`>=`)
- **Operadores lógicos** — verificação de condições de ataque com `and`
- **Concatenação** — montagem de mensagens com `.format()`
- **Entrada de dados** — uso de `input()` para receber o nome do personagem

## 💻 Como executar

Você precisa ter o [Python 3](https://www.python.org/downloads/) instalado.

```bash
python ficha_aventureiro.py
```

## 📄 Exemplo de saída

```
Digite o nome do seu personagem: Arion

==== Ficha do aventureiro ====
Nome: Arion
Nível: 7
Vida: 80 | Mana: 30
Status: Vivo

Pode entrar na masmorra? False
Pode atacar? True
```

## 🗂️ Código

```python
nome = str(input('Digite o nome do seu personagem: '))
nivel = 7
vida = 80
status = 'Vivo'
mana = 30

desbloquear_nivel = nivel >= 20
verificador_ataque = (status == 'Vivo') and (mana > 0)

print('{:=>4} Ficha do aventureiro {:=<4}'.format(' ', ' '))
print('Nome: {}\nNível: {}\nVida: {} | Mana: {}\nStatus: {}'.format(nome, nivel, vida, mana, status))
print('Pode entrar na masmorra? {}\nPode atacar? {}'.format(desbloquear_nivel, verificador_ataque))
```

---

Projeto feito com Python 3 como parte dos estudos iniciais da linguagem.