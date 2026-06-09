# Lista de Compras com Itens Essenciais

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluido-2E7D32?style=for-the-badge)
![Projeto](https://img.shields.io/badge/Projeto-Console_App-111827?style=for-the-badge)
![Nivel](https://img.shields.io/badge/Nivel-Iniciante_ao_Intermediario-F59E0B?style=for-the-badge)

Um projeto simples, funcional e educativo desenvolvido em **Python**, com o objetivo de criar uma lista de compras interativa via terminal e verificar automaticamente se os principais itens essenciais foram adicionados.

O programa permite que o usuario informe os produtos que deseja comprar, finalize a entrada de dados quando quiser e receba, ao final, um resumo numerado da lista junto com a verificacao dos itens essenciais que ainda estao faltando.

<p align="center">
  <img src="assets/preview.svg" alt="Preview do projeto Lista de Compras" width="720">
</p>

---

## Sumario

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Funciona](#como-funciona)
- [Exemplo de Execucao](#exemplo-de-execucao)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Conceitos Praticados](#conceitos-praticados)
- [Possiveis Melhorias](#possiveis-melhorias)
- [Autor](#autor)

---

## Sobre o Projeto

Este projeto foi criado para praticar fundamentos importantes da linguagem Python por meio de um problema comum do dia a dia: montar uma lista de compras.

A aplicacao trabalha com uma lista fixa de itens considerados essenciais:

```python
itens_essenciais = ('Arroz', 'Feijao', 'Oleo', 'Sal', 'Cafe')
```

Durante a execucao, o usuario pode digitar quantos itens quiser. Ao finalizar, o programa exibe a lista completa e informa quais itens essenciais nao foram incluidos.

Esse tipo de projeto e excelente para consolidar conceitos como:

- Entrada de dados pelo usuario
- Estruturas de repeticao
- Tuplas
- Listas
- Condicionais
- Comparacao de dados
- Enumeracao de itens
- Organizacao da saida no terminal

---

## Funcionalidades

O sistema possui as seguintes funcionalidades:

- Exibe uma lista inicial com os itens essenciais.
- Permite adicionar itens personalizados a lista de compras.
- Finaliza a entrada de dados quando o usuario digita `fim`.
- Mostra todos os itens adicionados em formato numerado.
- Exibe o total de itens cadastrados.
- Verifica automaticamente quais itens essenciais estao faltando.
- Informa quando todos os itens essenciais foram adicionados.

---

## Tecnologias Utilizadas

Este projeto foi desenvolvido com:

- **Python 3**
- Terminal / Prompt de Comando
- Recursos nativos da linguagem, sem bibliotecas externas

Nao e necessario instalar dependencias adicionais.

---

## Como Funciona

O funcionamento do programa pode ser dividido em quatro etapas principais:

### 1. Definicao dos itens essenciais

O programa inicia com uma tupla contendo produtos considerados indispensaveis em uma compra basica.

```python
itens_essenciais = ('Arroz', 'Feijao', 'Oleo', 'Sal', 'Cafe')
```

Foi utilizada uma **tupla** porque esses itens representam uma colecao fixa, ou seja, nao precisam ser alterados durante a execucao do programa.

### 2. Entrada dos itens pelo usuario

O usuario digita os produtos um por vez. Cada item informado e armazenado em uma lista chamada `lista`.

```python
while True:
    carrinho = input('Digite um item ou "fim" para finalizar as compras: ').strip()

    if carrinho.lower() == 'fim':
        break

    lista.append(carrinho)
```

O loop continua executando ate que o usuario digite `fim`.

### 3. Exibicao da lista final

Ao finalizar, o programa percorre os itens adicionados e exibe cada um com uma numeracao.

```python
for indice, item in enumerate(lista, start=1):
    print(f'{indice}. {item}')
```

O uso de `enumerate()` deixa a apresentacao mais organizada e facilita a leitura da lista.

### 4. Verificacao dos itens faltantes

Depois de montar a lista, o programa compara os itens digitados com os itens essenciais.

```python
for item in itens_essenciais:
    if item not in lista:
        faltando.append(item)
```

Se algum item essencial nao estiver presente, ele sera adicionado a lista `faltando` e exibido ao usuario.

---

## Exemplo de Execucao

```text
======= LISTA DE COMPRAS =======
========== ITENS ESSENCIAIS ============
Arroz
Feijao
Oleo
Sal
Cafe

Digite um item ou "fim" para finalizar as compras: Arroz
Digite um item ou "fim" para finalizar as compras: Cafe
Digite um item ou "fim" para finalizar as compras: Leite
Digite um item ou "fim" para finalizar as compras: fim

======= SUA LISTA =======
1. Arroz
2. Cafe
3. Leite
Total: 3 itens

Essenciais faltando na sua lista:
-> Feijao
-> Oleo
-> Sal
```

---

## Estrutura do Projeto

Uma estrutura simples recomendada para este repositorio:

```text
lista-de-compras/
├── assets/
│   └── preview.svg
├── main.py
└── README.md
```

Descricao dos arquivos:

| Arquivo | Descricao |
| --- | --- |
| `main.py` | Arquivo principal contendo o codigo do programa. |
| `README.md` | Documentacao completa do projeto. |
| `assets/preview.svg` | Imagem ilustrativa usada na documentacao. |

---

## Como Executar

### 1. Clone o repositorio

```bash
git clone https://github.com/seu-usuario/lista-de-compras.git
```

### 2. Acesse a pasta do projeto

```bash
cd lista-de-compras
```

### 3. Execute o programa

```bash
python main.py
```

Em alguns sistemas, pode ser necessario usar:

```bash
python3 main.py
```

---

## Codigo Principal

```python
print('======= LISTA DE COMPRAS =======')

itens_essenciais = ('Arroz', 'Feijao', 'Oleo', 'Sal', 'Cafe')
faltando = []
lista = []

print('========== ITENS ESSENCIAIS ============')
for item in itens_essenciais:
    print(f'{item}')

while True:
    carrinho = str(input('Digite um item ou "fim" para finalizar as compras: ')).strip()

    if carrinho.lower() == 'fim':
        break

    lista.append(carrinho)

print('======= SUA LISTA =======')
for indice, item in enumerate(lista, start=1):
    print(f'{indice}. {item}')

print(f'Total: {len(lista)} itens')

for item in itens_essenciais:
    if item not in lista:
        faltando.append(item)

if len(faltando) == 0:
    print('Parabens, nao ha nada faltando na sua lista')
else:
    print('Essenciais faltando na sua lista:')
    for item in faltando:
        print(f'-> {item}')
```

---

## Conceitos Praticados

Este projeto reforca diversos conceitos fundamentais de programacao:

| Conceito | Aplicacao no projeto |
| --- | --- |
| Variaveis | Armazenam listas, itens e valores digitados pelo usuario. |
| Tuplas | Guardam os itens essenciais que nao precisam ser alterados. |
| Listas | Armazenam os produtos adicionados e os itens faltantes. |
| `while True` | Mantem o programa recebendo itens ate o usuario finalizar. |
| `break` | Encerra o loop quando o usuario digita `fim`. |
| `for` | Percorre os itens essenciais e os itens da lista. |
| `if / else` | Controla as verificacoes e mensagens finais. |
| `enumerate()` | Exibe os itens da lista com numeracao. |
| `len()` | Calcula o total de itens adicionados. |
| `.strip()` | Remove espacos extras no inicio e no fim da entrada. |
| `.lower()` | Permite reconhecer `fim`, `FIM`, `Fim` e outras variacoes. |

---

## Possiveis Melhorias

Algumas evolucoes interessantes para futuras versoes:

- Comparar itens ignorando diferencas entre maiusculas e minusculas.
- Remover acentos para aceitar entradas como `oleo` e `óleo`.
- Impedir que itens vazios sejam adicionados.
- Evitar produtos duplicados na lista.
- Permitir remover itens antes de finalizar.
- Separar o codigo em funcoes.
- Salvar a lista em um arquivo `.txt`.
- Criar uma interface grafica simples.
- Adicionar testes automatizados.

---

## Aprendizados

Com este projeto, foi possivel praticar a construcao de um programa interativo completo, desde a entrada de dados ate a exibicao de um resultado final organizado.

Mesmo sendo um projeto simples, ele representa uma base importante para evoluir em Python, pois trabalha com logica, colecoes de dados, loops, condicionais e validacao de informacoes.

---

## Autor

Desenvolvido por **Ruan**.

Se este projeto te ajudou ou serviu de inspiracao, deixe uma estrela no repositorio.