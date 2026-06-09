print('======= LISTA DE COMPRAS =======')
essential_items = ('Arroz','Feijão','Óleo','Sal','Café')
missing = []

shopping_list = []
print('========== ITENS ESSENCIAIS ============')
for item in essential_items:
     print(f'{item}')



while True:
    cart = str(input('Digite um item ou "fim" para finalizar as compras: ')).strip()
    if cart.lower() == 'fim':
        break
    shopping_list.append(cart)



print('======= SUA LISTA =======')
for index, item in enumerate(shopping_list, start=1):
    print(f'{index}. {item}')
print(f'Total: {len(shopping_list)} itens')

for i in essential_items:
   if i not in shopping_list:
     missing.append(i)

if len(missing) == 0:
    print('Parábens, não há nada faltando na sua lista')
else:
    print('⚠ Essenciais faltando na sua lista:')
    for item in missing:
        print(f'→ {item}')

