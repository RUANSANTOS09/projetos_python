# Analise de Vendas com Funcoes em Python

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluido-2E7D32?style=for-the-badge)
![Conceito](https://img.shields.io/badge/Conceito-Funcoes-7C3AED?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Tipo-Console_App-111827?style=for-the-badge)

Projeto desenvolvido em **Python** para praticar o uso de **funcoes** na organizacao de uma rotina simples de tratamento e analise de vendas.

A aplicacao recebe uma lista com valores de vendas, remove dados invalidos, elimina valores duplicados e gera um pequeno relatorio estatistico com media, maior venda e menor venda.

Este projeto foi criado como exercicio de estudo para reforcar a importancia de dividir um problema em partes menores, reutilizaveis e mais faceis de entender.

<p align="center">
  <img src="assets/preview.svg" alt="Preview do projeto Analise de Vendas com Funcoes" width="780">
</p>

---

## Sumario

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivo](#objetivo)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Funciona](#como-funciona)
- [Fluxo da Aplicacao](#fluxo-da-aplicacao)
- [Exemplo de Execucao](#exemplo-de-execucao)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Conceitos Praticados](#conceitos-praticados)
- [Codigo Principal](#codigo-principal)
- [Possiveis Melhorias](#possiveis-melhorias)
- [Autor](#autor)

---

## Sobre o Projeto

O **Analise de Vendas com Funcoes em Python** e um projeto de terminal que demonstra como organizar um programa em funcoes pequenas, cada uma com uma responsabilidade especifica.

O codigo trabalha com uma lista inicial contendo valores validos e invalidos:

```python
list_n = [1000, None, 0, -1, 1000, 1000, 4000, 5000]
```

Essa lista possui:

- Valores positivos, que representam vendas validas.
- `None`, representando ausencia de valor.
- `0`, que nao e considerado uma venda valida.
- Valor negativo, que tambem deve ser descartado.
- Valores duplicados, que podem ser removidos antes da analise final.

A partir dessa lista, o programa realiza tres etapas principais:

- Limpeza dos dados.
- Remocao de duplicados.
- Analise estatistica.

---

## Objetivo

O objetivo principal deste projeto e praticar **funcoes em Python**.

Cada funcao foi criada para resolver uma parte especifica do problema:

| Funcao | Responsabilidade |
| --- | --- |
| `clean_sale()` | Filtrar apenas vendas validas. |
| `remove_duplicates()` | Remover valores repetidos. |
| `analyze_sales()` | Calcular media, maior venda e menor venda. |

Essa separacao deixa o codigo mais organizado e ajuda a aplicar um principio importante da programacao: cada bloco deve ter uma responsabilidade clara.

---

## Funcionalidades

O projeto possui as seguintes funcionalidades:

- Recebe uma lista de vendas com dados misturados.
- Remove valores `None`.
- Remove valores iguais a zero.
- Remove valores negativos.
- Mantem apenas valores positivos.
- Remove vendas duplicadas usando `set`.
- Calcula a media das vendas.
- Identifica a maior venda.
- Identifica a menor venda.
- Retorna os resultados em formato de dicionario.
- Exibe o relatorio final no terminal.

---

## Tecnologias Utilizadas

Este projeto foi desenvolvido com:

| Tecnologia | Uso no projeto |
| --- | --- |
| Python 3 | Linguagem principal da aplicacao. |
| Funcoes | Organizacao das etapas do programa. |
| Listas | Armazenamento dos valores de vendas. |
| Sets | Remocao de valores duplicados. |
| Dicionarios | Retorno estruturado do relatorio final. |
| Terminal | Exibicao dos resultados. |

O projeto nao utiliza bibliotecas externas.

---

## Como Funciona

O programa foi dividido em tres funcoes principais.

### 1. Funcao `clean_sale()`

```python
def clean_sale(val):
    valid_values = []

    for number in val:
        if number is not None and number > 0:
            valid_values.append(number)

    return valid_values
```

Essa funcao recebe uma lista e retorna apenas os valores considerados validos.

Um valor e considerado valido quando:

- Nao e `None`.
- E maior que `0`.

Com isso, a funcao remove dados ausentes, zeros e numeros negativos.

### 2. Funcao `remove_duplicates()`

```python
def remove_duplicates(val2):
    return set(val2)
```

Essa funcao recebe a lista ja limpa e converte seus valores para um `set`.

Em Python, um `set` nao permite elementos duplicados. Por isso, valores repetidos sao removidos automaticamente.

Exemplo:

```python
[1000, 1000, 1000, 4000, 5000]
```

Depois da conversao:

```python
{1000, 4000, 5000}
```

### 3. Funcao `analyze_sales()`

```python
def analyze_sales(val3):
    return {
        'average': sum(val3) / len(val3),
        'max_sale': max(val3),
        'min_sale': min(val3)
    }
```

Essa funcao recebe os valores tratados e retorna um dicionario com tres informacoes:

| Chave | Significado |
| --- | --- |
| `average` | Media dos valores analisados. |
| `max_sale` | Maior venda encontrada. |
| `min_sale` | Menor venda encontrada. |

O uso de dicionario torna o resultado mais organizado e facil de percorrer.

---

## Fluxo da Aplicacao

O fluxo do projeto pode ser representado assim:

```text
Lista original
     |
     v
clean_sale()
     |
     v
Vendas validas
     |
     v
remove_duplicates()
     |
     v
Vendas unicas
     |
     v
analyze_sales()
     |
     v
Relatorio final
```

Esse fluxo mostra como as funcoes trabalham em sequencia, cada uma preparando os dados para a proxima etapa.

---

## Exemplo de Execucao

Considerando a lista original:

```python
[1000, None, 0, -1, 1000, 1000, 4000, 5000]
```

A primeira etapa remove os valores invalidos:

```text
[1000, 1000, 1000, 4000, 5000]
```

A segunda etapa remove os duplicados:

```text
{1000, 4000, 5000}
```

O relatorio final exibe:

```text
average : 3333.3333333333335
max_sale : 5000
min_sale : 1000
```

---

## Estrutura do Projeto

Estrutura recomendada para o repositorio:

```text
analise-vendas-funcoes/
├── assets/
│   └── preview.svg
├── main.py
└── README.md
```

| Arquivo | Descricao |
| --- | --- |
| `main.py` | Arquivo principal contendo as funcoes e a execucao do programa. |
| `README.md` | Documentacao completa do projeto. |
| `assets/preview.svg` | Imagem de preview utilizada no README. |

---

## Como Executar

### 1. Clone o repositorio

```bash
git clone https://github.com/seu-usuario/analise-vendas-funcoes.git
```

### 2. Acesse a pasta do projeto

```bash
cd analise-vendas-funcoes
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

Este projeto reforca conceitos essenciais da linguagem Python.

| Conceito | Aplicacao no projeto |
| --- | --- |
| Funcoes | Separacao do codigo em blocos reutilizaveis. |
| Parametros | Cada funcao recebe dados para processar. |
| Retorno | As funcoes devolvem valores tratados ou analisados. |
| Listas | Armazenam os valores originais e os valores limpos. |
| `for` | Percorre os valores da lista original. |
| Condicionais | Validam se cada valor deve ser mantido. |
| `None` | Representa ausencia de valor. |
| `set` | Remove valores duplicados. |
| Dicionarios | Organizam o resultado final da analise. |
| `sum()` | Soma os valores analisados. |
| `len()` | Conta a quantidade de valores. |
| `max()` | Identifica o maior valor. |
| `min()` | Identifica o menor valor. |
| `.items()` | Percorre o dicionario do relatorio final. |

---

## Codigo Principal

```python
def clean_sale(val):
    valid_values = []

    for number in val:
        if number is not None and number > 0:
            valid_values.append(number)

    return valid_values


list_n = [1000, None, 0, -1, 1000, 1000, 4000, 5000]
clean = clean_sale(list_n)
print(clean)


def remove_duplicates(val2):
    return set(val2)


unique_sales = remove_duplicates(clean)
print(unique_sales)


def analyze_sales(val3):
    return {
        'average': sum(val3) / len(val3),
        'max_sale': max(val3),
        'min_sale': min(val3)
    }


relator = analyze_sales(unique_sales)

for key, value in relator.items():
    print(f'{key} : {value}')
```

---

## Possiveis Melhorias

Este projeto pode evoluir com algumas melhorias interessantes:

- Tratar o caso em que a lista final fica vazia.
- Retornar uma lista ordenada depois de remover duplicados.
- Arredondar a media para duas casas decimais.
- Renomear `relator` para `report`, mantendo um padrao em ingles.
- Criar uma funcao principal `main()`.
- Separar a exibicao dos resultados em uma funcao propria.
- Adicionar type hints nas funcoes.
- Criar testes automatizados para cada funcao.
- Permitir que o usuario digite os valores pelo terminal.
- Salvar o relatorio final em arquivo `.txt`, `.csv` ou `.json`.

---

## Observacoes Tecnicas

O projeto utiliza `set` para remover duplicados. Essa escolha e eficiente e simples, mas vale observar que conjuntos nao garantem a mesma ordem dos elementos da lista original.

Caso a ordem das vendas seja importante, uma melhoria futura seria usar outra estrategia para remover duplicados preservando a ordem.

Tambem e importante considerar que a funcao `analyze_sales()` depende de uma colecao com pelo menos um valor. Se a lista estiver vazia, funcoes como `max()`, `min()` e a divisao por `len()` podem gerar erro. Esse e um bom ponto para evoluir o projeto com validacao.

---

## Aprendizados

Este projeto mostra como funcoes ajudam a transformar um codigo simples em uma solucao mais organizada.

Ao separar a limpeza, a remocao de duplicados e a analise em funcoes diferentes, o programa fica mais facil de entender, testar e melhorar.

Essa forma de organizar o codigo e uma base importante para projetos maiores, onde clareza e manutencao fazem muita diferenca.

---

## Autor

Desenvolvido por **Ruan**.

Projeto criado como parte dos estudos em Python, com foco em praticar funcoes, tratamento de dados e organizacao de codigo.
