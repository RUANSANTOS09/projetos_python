# ================================================
# Lojinha Python
# Autor: (Ruan)
# Descrição: Sistema de compras no terminal com
#            seções, devoluções e resumo de compras.
# ================================================

transaction_counter = 0
total_spent = 0
total_refunded = 0
balance = float(input('Digite seu saldo atual: R$ '))
while True:
    print('===== Lojinha Python =====')
    option = int(input('[1] Comprar\n[2] Devolver\n[3] Resumo\n[4] Sair\nDigite um número: '))
#==================== Comprar ======================
    if(option == 1):
        while True:
            print('\n====== Mercado =========')
            purchase_option = int(input('[1] Seção Frios\n[2] Seção Verduras\n[3] Seção Frutas\n[4] Seção Produtos de Limpeza\n[5] Sair\nDigite um número: '))
            if(purchase_option == 1):
                print('\n=========== SEÇÃO FRIOS ===========')
                while True:
                    frozen_option = int(input('[1] Peixe Tilápia (10.00 R$ 1Kg) \n[2] Coxinha Congelada (R$ 15.00 1kg)\n[3] Pizza Frango com Catupiry Séara (R$ 15.89)\n[4] Confirmar e voltar\nDigite um número: '))
                    if(frozen_option == 1):
                        fish = 10
                        if(fish <= balance):
                           balance -= fish
                           total_spent += fish
                           transaction_counter += 1
                           print(f'Você comprou 1kg de Peixe e totalizou R${fish:.2f}' )
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    elif(frozen_option == 2):
                        chicken_croquette = 15
                        if(chicken_croquette <= balance):
                            balance -= chicken_croquette
                            total_spent += chicken_croquette
                            transaction_counter += 1
                            print(f'Você comprou 1kg de Coxinha e totalizou R${chicken_croquette:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    elif(frozen_option == 3):
                        pizza = 15.89
                        if(pizza <= balance):
                            balance -= pizza
                            total_spent += pizza
                            transaction_counter += 1
                            print(f'Você comprou Pizza com Catupiry Seara e totalizou R${pizza:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    else:
                        break
            elif(purchase_option == 2):
                print('\n=========== SEÇÃO VERDURAS ===========')
                while True:
                    vegetable_option = int(input('[1] 1 Kg Tomate R$ 8.00\n[2] 1 kg Cenoura R$ 4.50\n[3] 1 kg Cebola R$ 5.00\n[4] Confirmar e voltar\nDigite um número: '))
                    if(vegetable_option == 1):
                        tomato = 8.00
                        if(tomato <= balance):
                            balance -= tomato
                            total_spent += tomato
                            transaction_counter += 1
                            print(f'Você comprou tomate e totalizou R${tomato:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    elif(vegetable_option == 2):
                        carrot = 4.50
                        if(carrot <= balance):
                            balance -= carrot
                            total_spent += carrot
                            transaction_counter += 1
                            print(f'Você comprou cenoura e totalizou R${carrot:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    elif(vegetable_option == 3):
                        onion = 5.00
                        if(onion <= balance):
                            balance -= onion
                            total_spent += onion
                            transaction_counter += 1
                            print(f'Você comprou cebola e totalizou R${onion:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    else:
                        break
            elif(purchase_option == 3):
                while True:
                    print('\n=========== SEÇÃO FRUTAS ===========')
                    fruit_option = int(input(f'[1] Banana Prata R$ 6.00\n[2] Laranja Pêra R$ 5.00\n[3] Maçã Nacional R$ 10.00\n[4] Confirmar e voltar\nDigite um número: '))
                    if(fruit_option == 1):
                        banana = 6.00
                        if(banana <= balance):
                            balance -= banana
                            total_spent += banana
                            transaction_counter += 1
                            print(f'Você comprou banana e totalizou R${banana:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    elif(fruit_option == 2):
                        orange = 5.00
                        if(orange <= balance):
                            balance -= orange
                            total_spent += orange
                            transaction_counter += 1
                            print(f'Você comprou laranja e totalizou R${orange:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    elif(fruit_option == 3):
                        apple = 10.00
                        if(apple <= balance):
                            balance -= apple
                            total_spent += apple
                            transaction_counter += 1
                            print(f'Você comprou maçã e totalizou R${apple:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    else:
                        break
            elif(purchase_option == 4):
                while True:
                    print('\n=========== SEÇÃO PRODUTOS DE LIMPEZA ===========')
                    cleaning_option = int(input('[1] Detergente (500ml) R$ 4.50\n[2] Sabão em pó 1kg R$ 10.00\n[3] Amaciante de Roupas (2L) R$10.00\n[4] Confirmar e voltar\nDigite um número: '))
                    if(cleaning_option == 1):
                        dish_soap = 4.50
                        if(dish_soap <= balance):
                            balance -= dish_soap
                            total_spent += dish_soap
                            transaction_counter += 1
                            print(f'Você comprou detergente e totalizou R${dish_soap:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    elif(cleaning_option == 2):
                        laundry_powder = 10.00
                        if(laundry_powder <= balance):
                          balance -= laundry_powder
                          total_spent += laundry_powder
                          transaction_counter += 1
                          print(f'Você comprou sabao e totalizou R${laundry_powder:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    elif(cleaning_option == 3):
                        fabric_softener = 10.00
                        if(fabric_softener <= balance):
                          balance -= fabric_softener
                          total_spent += fabric_softener
                          transaction_counter += 1
                          print(f'Você comprou amaciante de roupas e totalizou R${fabric_softener:.2f}')
                        else:
                            print(f'SEU SALDO É R${balance:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${balance:.2f}\n')
                    else:
                        break
            else:
                break

#============================= Devolver ====================
    elif(option == 2):
        refund_amount = float(input('Digite o valor da devolução: R$ '))
        balance += refund_amount
        total_refunded += refund_amount
        transaction_counter += 1
        print(f'Saldo atual: R${balance:.2f}')
    elif(option == 3):
        print(f'Total gasto: R${total_spent:.2f}')
        print(f'Total devolvido: R${total_refunded:.2f}')
        print(f'Quantidade de transações: {transaction_counter}')
        print(f'Saldo atual: R${balance:.2f}')
    else:
        break

print('Obrigado por comprar na nossa loja :)')
print('========================')