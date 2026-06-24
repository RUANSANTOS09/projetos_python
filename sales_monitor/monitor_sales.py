cancelled_sales = []
approved_sales = []
cancelled = 0
approved = 0
sales = [
    'CONFIRMADA: Notebook - R$ 2500\n',
    'CANCELADA: Mouse - R$ 50\n',
    'CONFIRMADA: Teclado - R$ 120\n',
    'CANCELADA: Monitor - R$ 800\n',
    'CONFIRMADA: Webcam - R$ 150\n',
    'CANCELADA: Headset - R$ 200\n'
]
with open('sales.txt', 'w', encoding='utf-8') as s:
    s.writelines(sales)

with open('sales.txt', 'r', encoding='utf-8') as sales_rd:
    f = sales_rd.readlines()
    for i, v in enumerate(f, start = 1):
        if v.startswith('CANCELADA:'):
            cancelled += 1
            cancelled_sales.append(f'{i}: {v.rstrip()}\n')
        else:
            approved += 1
            approved_sales.append(f'{i}: {v.rstrip()}\n')
    approved_sales.append(f'\nVendas aprovadas: {approved}\n')
    cancelled_sales.append(f'\nVendas canceladas: {cancelled}')


with open('cancelled_sales.txt', 'w', encoding='utf-8') as c:
    c.writelines(cancelled_sales)
    for sale in cancelled_sales:
        print(sale)

with open('approved_sales.txt', 'w', encoding='utf-8') as a:
    a.writelines(approved_sales)
    for sale in approved_sales:
        print(sale)