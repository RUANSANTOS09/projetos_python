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

orcamento_total = float(input('\nDigite seu orçamento total: R$ '))

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
    print(f'\nVoce estourou o orçamento em R$ {excesso:.2f}.')
else:
    sobra = orcamento_total - total_geral
    print(f'\nOtimo! Voce ficou R$ {sobra:.2f} dentro do orçamento.')


