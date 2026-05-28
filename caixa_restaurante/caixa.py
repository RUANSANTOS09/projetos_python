#Menu
name = input('Qual o seu nome: ')
order = input('Escolha seu prato (X-Burguer / Pizza / Suco): ').lower()
member_check = input('É sócio do restaurante? (s/n): ').upper()
payment = int(input('Forma de pagamento - Cartão (1) | Dinheiro (2): '))
final_price = 0
xburger = 18.00
pizza = 35.00
juice = 8.00
print('{:->40}'.format(' '))
if(order.lower() == 'pizza'):
    print('Olá, {}! Você pediu {} -- R${:.2f}'.format(name, order, pizza))
elif(order.lower() == 'x-burguer' or order.lower() == 'xburguer'):
    print('Olá, {}! Você pediu {} -- R${:.2f}'.format(name, order, xburger))
elif(order.lower() == 'suco'):
    print('Olá, {}! Você pediu {} -- R${:.2f}'.format(name, order, juice))
else:
    print('Error: digite como mostra o cardapio. xburguer, pizza ou suco')


#verifica se o cliente é sócio ou não
if(order == 'pizza' and member_check.upper() == 'S'):
    price = 35.00
    member_discount = price * 0.15
    final_price = price - member_discount
    print('Valor original: R${:.2f}\nDesconto de sócio (15%): R${:.2f}\nTotal a pagar: R${:.2f} '.format(price, member_discount, final_price))
elif(order == 'pizza'):
    final_price = 35.00
    print('Valor original: R${:.2f}\nSem desconto\nTotal a pagar: R${:.2f}'.format(final_price, final_price))
elif((order == 'x-burguer' or order == 'xburguer') and member_check.upper() == 'S'):
    price = 18.00
    member_discount = price * 0.15
    final_price = price - member_discount
    print('Valor original: R${:.2f}\nDesconto de sócio (15%): R${:.2f}\nTotal a pagar: R${:.2f} '.format(price, member_discount, final_price))
elif(order == 'x-burguer' or order == 'xburguer'):
    final_price = 18.00
    print('Valor original: R${:.2f}\nSem desconto\nTotal a pagar: R${:.2f}'.format(final_price, final_price))
elif(order == 'suco' and member_check.upper() == 'S'):
    price = 8.00
    member_discount = price * 0.15
    final_price = price - member_discount
    print('Valor original: R${:.2f}\nDesconto de sócio (15%): R${:.2f}\nTotal a pagar: {:.2f} '.format(price, member_discount, final_price))
elif(order == 'suco'):
    final_price = 8.00
    print('Valor original: R${:.2f}\nSem desconto\nTotal a pagar: R${:.2f}'.format(final_price, final_price))
else:
    print('Error: digite o que temos no cardapio')


#Ganha sobremesa gratis?
free_dessert = payment == 2 and final_price > 30
if(free_dessert):
    print('Sobremesa grátis? Sim')
else:
    print('Sobremesa grátis? {}'.format(free_dessert))

print('{:->40}'.format(' '))