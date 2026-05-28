import math

print('===== GERENCIADOR DE GASTOS - MARCO =====')

fixed_expenses = (
    ('Aluguel', 1200.00),
    ('Internet', 99.90),
    ('Academia', 80.00)
)

variable_expenses = []
fixed_values = []

print('\nGastos fixos do mes:')

for name, value in fixed_expenses:
    print(f'{name}: R$ {value:.2f}')
    fixed_values.append(value)

fixed_total = math.fsum(fixed_values)

print(f'\nTotal fixo: R$ {fixed_total:.2f}')

monthly_budget = float(input('\nDigite seu orçamento total: R$ '))

print('\n--- Registre seus gastos variaveis ---')

while True:
    expense_name = input('Nome do gasto ou "fim" para encerrar: ').strip()

    if expense_name.lower() == 'fim':
        break

    expense_value = float(input('Valor do gasto: R$ '))

    expense = (expense_name, expense_value)
    variable_expenses.append(expense)

print('\n===== RELATORIO FINAL =====')

variable_total = 0

if len(variable_expenses) > 0:
    print('\nGastos variaveis:')

    for name, value in variable_expenses:
        print(f'{name}: R$ {value:.2f}')
        variable_total += value

    average_expense = variable_total / len(variable_expenses)
else:
    print('\nNenhum gasto variavel foi registrado.')
    average_expense = 0

total_spent = fixed_total + variable_total

print(f'\nTotal fixo: R$ {fixed_total:.2f}')
print(f'Total variavel: R$ {variable_total:.2f}')
print(f'Media dos gastos variaveis: R$ {average_expense:.2f}')
print(f'TOTAL GERAL: R$ {total_spent:.2f}')

if total_spent > monthly_budget:
    overspent_amount = total_spent - monthly_budget
    print(f'\nVoce estourou o orçamento em R$ {overspent_amount:.2f}.')
else:
    remaining_budget = monthly_budget - total_spent
    print(f'\nOtimo! Voce ficou R$ {remaining_budget:.2f} dentro do orçamento.')


