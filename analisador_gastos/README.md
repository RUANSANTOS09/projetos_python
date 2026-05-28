# Gerenciador de Gastos - Marco

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluido-2E7D32?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Console_App-111827?style=for-the-badge)
![Categoria](https://img.shields.io/badge/Categoria-Financas_Pessoais-0F766E?style=for-the-badge)

Projeto desenvolvido em **Python** para auxiliar no controle financeiro mensal, permitindo registrar gastos fixos, adicionar gastos variaveis, calcular totais e verificar se o usuario ficou dentro ou fora do orcamento definido.

A aplicacao roda diretamente no terminal e foi criada com foco em praticar fundamentos importantes da linguagem Python por meio de um problema real: organizar despesas pessoais de forma simples, clara e objetiva.

<p align="center">
  <img src="assets/preview.svg" alt="Preview do Gerenciador de Gastos" width="760">
</p>

---

## Sumario

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivo](#objetivo)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
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

O **Gerenciador de Gastos - Marco** e uma aplicacao de linha de comando criada para simular um controle basico de despesas mensais.

O programa possui uma lista inicial de gastos fixos, solicita ao usuario o valor total disponivel para o mes e permite registrar gastos variaveis conforme a necessidade.

Ao final, o sistema gera um relatorio contendo:

- Total de gastos fixos.
- Total de gastos variaveis.
- Media dos gastos variaveis.
- Total geral gasto no mes.
- Comparacao entre o total gasto e o orcamento informado.
- Mensagem indicando se houve sobra ou estouro no orcamento.

Mesmo sendo um projeto simples, ele representa uma base muito importante para evoluir em Python, principalmente por trabalhar com entrada de dados, estruturas de repeticao, tuplas, listas, calculos numericos e tomada de decisao.

---

## Objetivo

O objetivo principal deste projeto e aplicar logica de programacao em um cenario financeiro pratico.

Ele pode ser usado como exercicio para entender como um programa recebe informacoes do usuario, processa valores, organiza dados e apresenta um resultado final de maneira legivel.

Este projeto tambem serve como ponto de partida para sistemas maiores, como:

- Controle financeiro pessoal.
- Aplicativo de orcamento mensal.
- Gerenciador de despesas domesticas.
- Relatorio financeiro automatizado.
- Sistema simples de planejamento de gastos.

---

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

- Exibe gastos fixos ja cadastrados.
- Calcula automaticamente o total dos gastos fixos.
- Solicita o orcamento total disponivel para o mes.
- Permite cadastrar gastos variaveis dinamicamente.
- Finaliza o cadastro quando o usuario digita `fim`.
- Lista todos os gastos variaveis registrados.
- Calcula o total dos gastos variaveis.
- Calcula a media dos gastos variaveis.
- Soma gastos fixos e variaveis para gerar o total geral.
- Compara o total geral com o orcamento informado.
- Informa se o usuario ficou dentro do orcamento ou se ultrapassou o limite.

---

## Tecnologias Utilizadas

Este projeto foi desenvolvido com:

| Tecnologia | Uso no projeto |
| --- | --- |
| Python 3 | Linguagem principal da aplicacao. |
| Modulo `math` | Utilizado para somar valores fixos com `math.fsum()`. |
| Terminal | Ambiente de execucao e interacao com o usuario. |

Nao ha dependencias externas. O projeto utiliza apenas recursos nativos do Python.

---

## Como Funciona

O fluxo da aplicacao foi dividido em etapas simples e bem definidas.

### 1. Importacao do modulo `math`

```python
import math
```

O modulo `math` e utilizado para acessar a funcao `fsum()`, que realiza somas de valores numericos com maior precisao do que a soma comum em alguns cenarios com numeros decimais.

### 2. Definicao dos gastos fixos

```python
gastos_fixos = (
    ('Aluguel', 1200.00),
    ('Internet', 99.90),
    ('Academia', 80.00)
)
```

Os gastos fixos foram armazenados em uma **tupla de tuplas**.

Essa escolha faz sentido porque esses dados representam despesas pre-definidas, que nao precisam ser alteradas durante a execucao do programa.

### 3. Exibicao e soma dos gastos fixos

```python
for nome, valor in gastos_fixos:
    print(f'{nome}: R$ {valor:.2f}')
    valores_fixos.append(valor)

total_fixo = math.fsum(valores_fixos)
```

O programa percorre todos os gastos fixos, exibe cada um no terminal e adiciona seus valores a uma lista auxiliar chamada `valores_fixos`.

Depois disso, a funcao `math.fsum()` calcula o total fixo do mes.

### 4. Registro do orcamento

```python
orcamento_total = float(input('Digite seu orcamento total: R$ '))
```

O usuario informa quanto possui disponivel para gastar no mes. Esse valor sera usado no final para verificar se o total de gastos ficou dentro ou fora do limite.

### 5. Cadastro dos gastos variaveis

```python
while True:
    nome_gasto = input('Nome do gasto ou "fim" para encerrar: ').strip()

    if nome_gasto.lower() == 'fim':
        break

    valor_gasto = float(input('Valor do gasto: R$ '))

    gasto = (nome_gasto, valor_gasto)
    gastos_variaveis.append(gasto)
```

O usuario pode registrar quantos gastos variaveis quiser.

Cada gasto e armazenado como uma tupla contendo:

- Nome do gasto.
- Valor do gasto.

Essas tuplas sao adicionadas na lista `gastos_variaveis`.

### 6. Geracao do relatorio final

No final da execucao, o programa mostra um relatorio consolidado com os totais calculados.

```python
total_geral = total_fixo + total_variavel
```

Depois, o sistema compara o total geral com o orcamento:

```python
if total_geral > orcamento_total:
    excesso = total_geral - orcamento_total
    print(f'Voce estourou o orcamento em R$ {excesso:.2f}.')
else:
    sobra = orcamento_total - total_geral
    print(f'Otimo! Voce ficou R$ {sobra:.2f} dentro do orcamento.')
```

---

## Exemplo de Execucao

```text
===== GERENCIADOR DE GASTOS - MARCO =====

Gastos fixos do mes:
Aluguel: R$ 1200.00
Internet: R$ 99.90
Academia: R$ 80.00

Total fixo: R$ 1379.90

Digite seu orcamento total: R$ 2500

--- Registre seus gastos variaveis ---
Nome do gasto ou "fim" para encerrar: Mercado
Valor do gasto: R$ 450
Nome do gasto ou "fim" para encerrar: Transporte
Valor do gasto: R$ 180
Nome do gasto ou "fim" para encerrar: Lazer
Valor do gasto: R$ 150
Nome do gasto ou "fim" para encerrar: fim

===== RELATORIO FINAL =====

Gastos variaveis:
Mercado: R$ 450.00
Transporte: R$ 180.00
Lazer: R$ 150.00

Total fixo: R$ 1379.90
Total variavel: R$ 780.00
Media dos gastos variaveis: R$ 260.00
TOTAL GERAL: R$ 2159.90

Otimo! Voce ficou R$ 340.10 dentro do orcamento.
```

---

## Estrutura do Projeto

Estrutura recomendada para o repositorio:

```text
gerenciador-de-gastos/
├── assets/
│   └── preview.svg
├── main.py
└── README.md
```

| Arquivo | Descricao |
| --- | --- |
| `main.py` | Arquivo principal com o codigo da aplicacao. |
| `README.md` | Documentacao completa do projeto. |
| `assets/preview.svg` | Imagem de preview exibida na documentacao. |

---

## Como Executar

### 1. Clone o repositorio

```bash
git clone https://github.com/seu-usuario/gerenciador-de-gastos.git
```

### 2. Acesse a pasta do projeto

```bash
cd gerenciador-de-gastos
```

### 3. Execute o arquivo principal

```bash
python main.py
```

Se o comando acima nao funcionar no seu sistema, tente:

```bash
python3 main.py
```

---

## Conceitos Praticados

Este projeto reforca conceitos essenciais da programacao com Python.

| Conceito | Aplicacao no projeto |
| --- | --- |
| `import` | Importa o modulo `math`. |
| Tuplas | Armazenam os gastos fixos e cada gasto variavel. |
| Listas | Guardam valores fixos e gastos variaveis cadastrados. |
| `for` | Percorre os gastos fixos e variaveis. |
| `while True` | Mantem o cadastro de gastos ativo ate o usuario encerrar. |
| `break` | Interrompe o loop quando o usuario digita `fim`. |
| `input()` | Recebe informacoes digitadas pelo usuario. |
| `float()` | Converte valores digitados em numeros decimais. |
| `.strip()` | Remove espacos extras da entrada do usuario. |
| `.lower()` | Padroniza a verificacao da palavra `fim`. |
| `len()` | Calcula a quantidade de gastos variaveis. |
| Condicionais | Verificam se houve sobra ou estouro no orcamento. |
| Formatacao monetaria | Exibe valores com duas casas decimais usando `:.2f`. |

---

## Codigo Principal

```python
import math

print('===== GERENCIADOR DE GASTOS - MARCO =====')

gastos_fixos = (
    ('Aluguel', 1200.00),
    ('Internet', 99.90),
    ('Academia', 80.00)
)

gastos_variaveis = []
valores_fixos = []

print('\nGastos fixos do mes:')

for nome, valor in gastos_fixos:
    print(f'{nome}: R$ {valor:.2f}')
    valores_fixos.append(valor)

total_fixo = math.fsum(valores_fixos)

print(f'\nTotal fixo: R$ {total_fixo:.2f}')

orcamento_total = float(input('\nDigite seu orcamento total: R$ '))

print('\n--- Registre seus gastos variaveis ---')

while True:
    nome_gasto = input('Nome do gasto ou "fim" para encerrar: ').strip()

    if nome_gasto.lower() == 'fim':
        break

    valor_gasto = float(input('Valor do gasto: R$ '))

    gasto = (nome_gasto, valor_gasto)
    gastos_variaveis.append(gasto)

print('\n===== RELATORIO FINAL =====')

total_variavel = 0

if len(gastos_variaveis) > 0:
    print('\nGastos variaveis:')

    for nome, valor in gastos_variaveis:
        print(f'{nome}: R$ {valor:.2f}')
        total_variavel += valor

    media_gastos = total_variavel / len(gastos_variaveis)
else:
    print('\nNenhum gasto variavel foi registrado.')
    media_gastos = 0

total_geral = total_fixo + total_variavel

print(f'\nTotal fixo: R$ {total_fixo:.2f}')
print(f'Total variavel: R$ {total_variavel:.2f}')
print(f'Media dos gastos variaveis: R$ {media_gastos:.2f}')
print(f'TOTAL GERAL: R$ {total_geral:.2f}')

if total_geral > orcamento_total:
    excesso = total_geral - orcamento_total
    print(f'\nVoce estourou o orcamento em R$ {excesso:.2f}.')
else:
    sobra = orcamento_total - total_geral
    print(f'\nOtimo! Voce ficou R$ {sobra:.2f} dentro do orcamento.')
```

---

## Possiveis Melhorias

Este projeto pode evoluir bastante com novas funcionalidades:

- Validar entradas para evitar erro quando o usuario digitar texto no lugar de numero.
- Impedir cadastro de gastos com valor negativo.
- Separar o codigo em funcoes.
- Criar categorias para os gastos variaveis.
- Exibir percentual do orcamento consumido.
- Salvar o relatorio em arquivo `.txt` ou `.csv`.
- Permitir editar ou remover gastos antes do relatorio final.
- Usar `decimal.Decimal` para calculos financeiros mais robustos.
- Criar testes automatizados.
- Desenvolver uma interface grafica ou versao web.

---

## Observacoes Tecnicas

Para fins de aprendizado, o projeto utiliza `float` para lidar com valores monetarios. Em aplicacoes financeiras reais, o ideal e utilizar `decimal.Decimal`, pois ele oferece mais controle sobre casas decimais e evita algumas imprecisoes comuns de numeros de ponto flutuante.

Ainda assim, para um projeto introdutorio de console, a implementacao atual e adequada para praticar logica, estruturas de dados e fluxo de execucao em Python.

---

## Autor

Desenvolvido por **Ruan**.

Este projeto faz parte da minha jornada de estudos em Python, com foco em criar solucoes simples, uteis e bem documentadas.
