# Analise de Vendas por Vendedor

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluido-2E7D32?style=for-the-badge)
![Conceito](https://img.shields.io/badge/Conceito-Dicionarios-7C3AED?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Console_App-111827?style=for-the-badge)

Projeto desenvolvido em **Python** para analisar o desempenho de vendedores a partir de metas fixas, listas de vendas e organizacao dos dados com **dicionarios**.

A aplicacao calcula o total vendido por cada vendedor, classifica o desempenho com base em metas, identifica o destaque do mes e apresenta a media geral da equipe.

Este projeto foi criado como exercicio pratico para treinar o uso de **dicionarios em Python**, alem de reforcar listas, tuplas, lacos de repeticao, condicionais, acumuladores e formatacao de valores monetarios.

<p align="center">
  <img src="assets/preview.svg" alt="Preview do projeto Analise de Vendas por Vendedor" width="780">
</p>

---

## Sumario

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivo](#objetivo)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como os Dados Sao Organizados](#como-os-dados-sao-organizados)
- [Como Funciona](#como-funciona)
- [Exemplo de Execucao](#exemplo-de-execucao)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Conceitos Praticados](#conceitos-praticados)
- [Codigo Principal](#codigo-principal)
- [Possiveis Melhorias](#possiveis-melhorias)
- [Autor](#autor)

---

## Sobre o Projeto

O **Analise de Vendas por Vendedor** e um programa de terminal que simula um relatorio simples de desempenho comercial.

O sistema possui uma equipe com tres vendedores:

- Ana
- Laura
- Pedro

Cada vendedor possui uma lista com valores de vendas realizadas no mes. Esses dados sao agrupados dentro de um dicionario, em que a chave representa o nome do vendedor e o valor representa a lista de vendas desse vendedor.

Com base nessas informacoes, o programa calcula:

- Total vendido por vendedor.
- Quantidade de vendas realizadas.
- Situacao de cada vendedor em relacao as metas.
- Total vendido pela equipe.
- Media de vendas da equipe.
- Vendedor com maior resultado no mes.

---

## Objetivo

O principal objetivo deste projeto e praticar **dicionarios em Python** dentro de um contexto realista.

Em vez de usar variaveis soltas para cada vendedor, o projeto organiza os dados em uma estrutura mais profissional:

```python
seller_data = {
   'Ana': ana_sales,
   'Laura': laura_sales,
   'Pedro': pedro_sales
}
```

Esse formato facilita a leitura, manutencao e evolucao do codigo, pois permite percorrer todos os vendedores usando apenas um loop.

---

## Funcionalidades

O programa possui as seguintes funcionalidades:

- Armazena metas fixas usando uma tupla.
- Separa meta minima e meta ideal com desempacotamento de tupla.
- Armazena as vendas de cada vendedor em listas.
- Organiza os vendedores e suas vendas em um dicionario.
- Percorre o dicionario com `.items()`.
- Calcula o total vendido individualmente.
- Classifica cada vendedor conforme o total vendido.
- Identifica quem bateu a meta ideal.
- Identifica quem bateu a meta minima.
- Identifica quem ficou abaixo da meta.
- Calcula o total geral vendido pela equipe.
- Calcula a media de vendas por vendedor.
- Identifica o destaque do mes com base no maior total vendido.

---

## Tecnologias Utilizadas

Este projeto foi desenvolvido com:

| Tecnologia | Uso no projeto |
| --- | --- |
| Python 3 | Linguagem principal da aplicacao. |
| Dicionarios | Organizacao dos vendedores e suas listas de vendas. |
| Listas | Armazenamento dos valores de vendas. |
| Tuplas | Armazenamento das metas fixas. |
| Terminal | Ambiente de execucao e exibicao do relatorio. |

O projeto nao utiliza bibliotecas externas.

---

## Como os Dados Sao Organizados

A parte mais importante do projeto e a organizacao dos vendedores dentro de um dicionario.

```python
seller_data = {
   'Ana': ana_sales,
   'Laura': laura_sales,
   'Pedro': pedro_sales
}
```

Nesse dicionario:

| Chave | Valor |
| --- | --- |
| `'Ana'` | Lista com as vendas da Ana. |
| `'Laura'` | Lista com as vendas da Laura. |
| `'Pedro'` | Lista com as vendas do Pedro. |

Cada chave representa o nome de um vendedor. Cada valor representa uma lista contendo as vendas realizadas por esse vendedor.

Essa estrutura e muito util porque permite que o programa percorra todos os vendedores de maneira dinamica:

```python
for name, value in seller_data.items():
    total_sales = sum(value)
```

O metodo `.items()` retorna pares compostos por chave e valor. Neste projeto:

- `name` recebe o nome do vendedor.
- `value` recebe a lista de vendas do vendedor.

---

## Como Funciona

O funcionamento do programa pode ser dividido em etapas.

### 1. Definicao das metas

```python
fixed_goals = (3000, 5000)
minimum_goal, ideal_goal = fixed_goals
```

O programa utiliza uma tupla para armazenar duas metas:

| Variavel | Valor | Significado |
| --- | --- | --- |
| `minimum_goal` | `3000` | Meta minima. |
| `ideal_goal` | `5000` | Meta ideal. |

O desempacotamento da tupla deixa o codigo mais legivel, pois cada meta recebe um nome claro.

### 2. Registro das vendas

```python
ana_sales = [1000, 1000, 1000, 2200]
laura_sales = [1000, 1000, 1100]
pedro_sales = [1000, 1400]
```

Cada lista representa as vendas realizadas por um vendedor.

Por exemplo, Ana possui quatro vendas registradas, enquanto Pedro possui duas.

### 3. Percorrendo os vendedores

```python
for name, value in seller_data.items():
    total_sales = sum(value)
```

O loop percorre todos os vendedores cadastrados no dicionario. Para cada vendedor, o programa soma sua lista de vendas usando `sum()`.

### 4. Classificacao por desempenho

O programa compara o total vendido com as metas estabelecidas:

```python
if total_sales >= ideal_goal:
    print('Bateu a meta ideal')
elif total_sales >= minimum_goal:
    print('Bateu a meta minima')
else:
    print('Abaixo da meta')
```

A classificacao segue esta regra:

| Total vendido | Situacao |
| --- | --- |
| Maior ou igual a `5000` | Bateu a meta ideal. |
| Maior ou igual a `3000` | Bateu a meta minima. |
| Menor que `3000` | Abaixo da meta. |

### 5. Identificacao do destaque do mes

```python
if total_sales > more_sales:
    more_sales = total_sales
    highlight_of_the_month = name
```

O programa compara o total de cada vendedor com o maior valor encontrado ate o momento.

Quando encontra um vendedor com resultado maior, atualiza:

- `more_sales`
- `highlight_of_the_month`

Assim, ao final da execucao, o sistema sabe quem foi o vendedor com maior faturamento.

### 6. Calculo da media da equipe

```python
average = total_team / len(seller_data)
```

A media da equipe e calculada dividindo o total vendido por todos os vendedores pela quantidade de vendedores cadastrados.

---

## Exemplo de Execucao

Considerando os dados atuais do projeto, a saida esperada e:

```text
Ana Vendas realizadas: 4 Total vendido : R$5200.00 Situacao : Bateu a meta ideal
Laura Vendas realizadas: 3 Total vendido : R$3100.00 Situacao : Bateu a meta minima
Pedro Vendas realizadas: 2 Total vendido : R$2400.00 Situacao : Abaixo da meta
Destaque do mes : Ana - R$5200.00
Media da equipe: R$3566.67
```

---

## Estrutura do Projeto

Estrutura recomendada para o repositorio:

```text
analise-vendas-vendedores/
├── assets/
│   └── preview.svg
├── main.py
└── README.md
```

| Arquivo | Descricao |
| --- | --- |
| `main.py` | Arquivo principal contendo a logica do programa. |
| `README.md` | Documentacao completa do projeto. |
| `assets/preview.svg` | Imagem de preview usada no README. |

---

## Como Executar

### 1. Clone o repositorio

```bash
git clone https://github.com/seu-usuario/analise-vendas-vendedores.git
```

### 2. Acesse a pasta do projeto

```bash
cd analise-vendas-vendedores
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

## Conceitos Praticados

Este projeto reforca diversos conceitos fundamentais de Python.

| Conceito | Aplicacao no projeto |
| --- | --- |
| Variaveis acumuladoras | `total_team` soma o total vendido pela equipe. |
| Strings | `highlight_of_the_month` armazena o nome do destaque. |
| Numeros | `more_sales` guarda o maior total encontrado. |
| Tuplas | `fixed_goals` armazena as metas fixas. |
| Desempacotamento | `minimum_goal, ideal_goal = fixed_goals`. |
| Listas | Cada vendedor possui uma lista de vendas. |
| Dicionarios | `seller_data` organiza vendedores e vendas. |
| `.items()` | Permite percorrer chaves e valores do dicionario. |
| `sum()` | Calcula o total de vendas de cada lista. |
| `len()` | Conta vendas e quantidade de vendedores. |
| Condicionais | Classificam o desempenho em relacao as metas. |
| Formatacao | Exibe valores monetarios com duas casas decimais. |

---

## Codigo Principal

```python
total_team = 0
highlight_of_the_month = ''
more_sales = 0

fixed_goals = (3000, 5000)
minimum_goal, ideal_goal = fixed_goals

ana_sales = [1000, 1000, 1000, 2200]
laura_sales = [1000, 1000, 1100]
pedro_sales = [1000, 1400]

seller_data = {
   'Ana': ana_sales,
   'Laura': laura_sales,
   'Pedro': pedro_sales
}

for name, value in seller_data.items():
    total_sales = sum(value)
    total_team += total_sales

    if total_sales >= ideal_goal:
        print(f'{name} Vendas realizadas: {len(value)} Total vendido : R${sum(value):.2f} Situacao : Bateu a meta ideal')
    elif total_sales >= minimum_goal:
        print(f'{name} Vendas realizadas: {len(value)} Total vendido : R${sum(value):.2f} Situacao : Bateu a meta minima')
    else:
        print(f'{name} Vendas realizadas: {len(value)} Total vendido : R${sum(value):.2f} Situacao : Abaixo da meta')

    if total_sales > more_sales:
        more_sales = total_sales
        highlight_of_the_month = name

average = total_team / len(seller_data)

print(f'Destaque do mes : {highlight_of_the_month} - R${more_sales:.2f}')
print(f'Media da equipe: R${average:.2f}')
```

---

## Possiveis Melhorias

Este projeto pode evoluir com novas funcionalidades:

- Permitir cadastrar vendedores dinamicamente pelo terminal.
- Permitir cadastrar vendas dinamicamente para cada vendedor.
- Criar um ranking ordenado por total vendido.
- Separar a logica em funcoes.
- Criar uma funcao especifica para classificar desempenho.
- Exibir percentual de atingimento da meta.
- Salvar o relatorio em `.txt`, `.csv` ou `.json`.
- Adicionar validacao para impedir valores negativos.
- Criar testes automatizados.
- Transformar o projeto em uma pequena aplicacao web.

---

## Aprendizados

Este projeto mostra como dicionarios tornam o codigo mais organizado quando existe uma relacao entre uma chave e um conjunto de dados.

No contexto do projeto, cada vendedor e uma chave, e cada lista de vendas e o valor associado a essa chave.

Essa forma de organizar os dados aproxima o codigo de situacoes reais, onde geralmente precisamos relacionar nomes, identificadores ou categorias a colecoes de informacoes.

---

## Autor

Desenvolvido por **Ruan**.

Projeto criado como parte dos estudos em Python, com foco em praticar dicionarios, estruturas de dados e logica de programacao aplicada a relatorios de vendas.