#Cardápio
nome = input('Qual o seu nome: ')
pedido = input('Escolha seu prato (X-Burguer / Pizza / Suco): ').lower()
verificador_socio = input('É sócio do restaurante? (s/n): ').upper() #Para aceitar n/s maiusculo ou minusculo
pagamento = int(input('Forma de pagamento - Cartão (1) | Dinheiro (2): '))
preco_final = 0
xburguer = 18.00
pizza = 35.00
suco = 8.00
print('{:->40}'.format(' '))
if(pedido.lower() == 'pizza'):
    print('Olá, {}! Você pediu {} -- R${:.2f}'.format(nome, pedido,pizza))
elif(pedido.lower() ==  'x-burguer' or pedido.lower() == 'xburguer'):
    print('Olá, {}! Você pediu {} -- R${:.2f}'.format(nome, pedido,xburguer))
elif(pedido.lower() == 'suco'):
    print('Olá, {}! Você pediu {} -- R${:.2f}'.format(nome, pedido,suco))
else:
    print('Error: digite como mostra o cardapio. xburguer, pizza ou suco')


#verifica se o cliente é sócio ou não
if(pedido == 'pizza' and verificador_socio.upper() == 'S'):
    preco = 35.00
    desconto_socio = preco * 0.15
    preco_final = preco - desconto_socio
    print('Valor original: R${:.2f}\nDesconto de sócio (15%): R${:.2f}\nTotal a pagar: R${:.2f} '.format(preco,desconto_socio,preco_final))
elif(pedido == 'pizza'):
    preco_final = 35.00
    print('Valor original: R${:.2f}\nSem desconto\nTotal a pagar: R${:.2f}'.format(preco_final, preco_final))
elif((pedido == 'x-burguer' or pedido == 'xburguer') and verificador_socio.upper() == 'S'):
    preco = 18.00
    desconto_socio = preco * 0.15
    preco_final = preco - desconto_socio
    print('Valor original: R${:.2f}\nDesconto de sócio (15%): R${:.2f}\nTotal a pagar: R${:.2f} '.format(preco,desconto_socio, preco_final))
elif(pedido == 'x-burguer' or pedido == 'xburguer'):
    preco_final = 18.00
    print('Valor original: R${:.2f}\nSem desconto\nTotal a pagar: R${:.2f}'.format(preco_final, preco_final))
elif(pedido == 'suco' and verificador_socio.upper() == 'S'):
    preco = 8.00
    desconto_socio = preco * 0.15
    preco_final = preco - desconto_socio
    print('Valor original: R${:.2f}\nDesconto de sócio (15%): R${:.2f}\nTotal a pagar: {:.2f} '.format(preco,desconto_socio, preco_final))
elif(pedido == 'suco'):
    preco_final = 8.00
    print('Valor original: R${:.2f}\nSem desconto\nTotal a pagar: R${:.2f}'.format(preco_final, preco_final))
else:
    print('Error: digite o que temos no cardapio')


#Ganha sobremesa gratis?
sobremesa_gratis = pagamento == 2 and preco_final > 30
if(sobremesa_gratis):
    print('Sobremesa grátis? Sim')
else:
    print('Sobremesa grátis? {}'.format(sobremesa_gratis))

print('{:->40}'.format(' '))