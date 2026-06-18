# 🗂️ Pipeline de Fontes de Dados — POO em Python

> Modelagem orientada a objetos de fontes de dados heterogêneas (arquivos CSV e APIs externas), simulando o componente de ingestão de um pipeline de dados real.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-7FB069?style=flat-square)
![Paradigma](https://img.shields.io/badge/Paradigma-POO-D4A574?style=flat-square)
![Licença](https://img.shields.io/badge/Licença-MIT-4A5550?style=flat-square)

---

## 📖 Sobre o projeto

Este projeto modela, em **Programação Orientada a Objetos**, diferentes **fontes de dados** que alimentam um pipeline — um cenário comum no dia a dia de Engenharia de Dados, onde múltiplas origens (arquivos, APIs, bancos) precisam ser representadas de forma consistente, mas com particularidades próprias.

A proposta nasceu como exercício de fixação dos pilares de POO — **encapsulamento**, **herança** e **polimorfismo** — aplicados a um contexto realista, e não a exemplos genéricos de sala de aula.

### Por que esse projeto existe

Em um pipeline de dados real, é comum precisar tratar fontes diferentes (um CSV, uma API, um banco) de forma **uniforme** no nível do código que as consome, enquanto cada uma mantém seu comportamento específico por baixo. Isso é exatamente o que herança e polimorfismo resolvem — e é o que este projeto demonstra na prática, em escala reduzida.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no projeto |
|---|---|
| **Encapsulamento** | Todos os atributos são privados (`__atributo`), acessados apenas via getters |
| **Herança** | `ArquivoCSV` e `APIExterna` herdam de `FonteDados` |
| **Polimorfismo** | As três classes compartilham o método `status()`, cada uma com um comportamento próprio |
| **`super()`** | Usado tanto no construtor quanto no método `status()`, reaproveitando a lógica da classe pai em vez de duplicá-la |
| **Separação de responsabilidades** | Métodos que alteram estado (`set_add_records`) são separados dos que apenas leem estado (`status`, getters) |

---

## 🏗️ Arquitetura

```
                ┌──────────────────────┐
                │      FonteDados       │
                │------------------------│
                │ - nome                │
                │ - total_registros     │
                │------------------------│
                │ + adicionar_registros()│
                │ + status()            │
                └───────────┬────────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
   ┌──────────▼───────────┐   ┌───────────▼────────────┐
   │      ArquivoCSV       │   │      APIExterna         │
   │------------------------│   │--------------------------│
   │ - delimitador          │   │ - limite_requisicoes     │
   │------------------------│   │--------------------------│
   │ + status() [override]  │   │ + requisicoes_disponiveis()│
   │                        │   │ + status() [override]    │
   └────────────────────────┘   └──────────────────────────┘
```

Cada subclasse **reaproveita** a lógica de `status()` da classe-mãe via `super().status()`, e apenas **complementa** a informação — sem duplicar código.

---

## 💻 Exemplo de uso

```python
# Criando uma fonte do tipo arquivo CSV
arquivo = ArquivoCSV("usuarios_sistema", ";")
arquivo.adicionar_registros(150)
print(arquivo.status())
# usuarios_sistema: 150 registros processados | delimitador: ;

# Criando uma fonte do tipo API externa
api = APIExterna("API Clima", limite_requisicoes=1000)
api.adicionar_registros(230)
print(api.status())
# API Clima: 230 registros processados | requisições disponíveis: 770
```

---

## ▶️ Como executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/nome-do-repositorio.git

# Acesse a pasta
cd nome-do-repositorio

# Execute o script
python main.py
```

**Pré-requisitos:** apenas Python 3.10 ou superior — sem dependências externas.

---

## 📂 Estrutura do repositório

```
.
├── main.py          # Código-fonte do projeto
└── README.md         # Este arquivo
```

---

## 🚀 Próximos passos

Este projeto faz parte de uma trilha de estudos contínua em direção à Engenharia de Dados. Possíveis evoluções futuras:

- [ ] Adicionar uma classe `BancoDeDados` como terceira fonte, reforçando o polimorfismo
- [ ] Persistir o `status()` de cada fonte em um arquivo de log
- [ ] Tratar exceções (ex: arquivo inexistente, limite de API excedido)
- [ ] Reescrever a ingestão usando **Pandas**, comparando a abordagem orientada a objetos com a abordagem orientada a dados

---

## 🛠️ Tecnologias

- **Python 3** — linguagem utilizada, sem bibliotecas externas

---

## 👤 Autor

Projeto desenvolvido como parte de estudos pessoais em **Python e Engenharia de Dados**.

Sinta-se livre para abrir uma *issue* com sugestões ou *forks* para experimentar variações do modelo.

---

<p align="center">
  <i>Construído estudo por estudo, exercício por exercício — rumo à Engenharia de Dados. 🛤️</i>
</p>
