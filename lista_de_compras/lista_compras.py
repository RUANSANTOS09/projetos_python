print('======= LISTA DE COMPRAS =======')
itens_essenciais = ('Arroz','Feijão','Óleo','Sal','Café')
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

for i in itens_essenciais:
   if i not in lista:
     faltando.append(i)

if len(faltando) == 0:
    print('Parábens, não há nada faltando na sua lista')
else:
    print('⚠ Essenciais faltando na sua lista:')
    for item in faltando:
        print(f'→ {item}')

