contador_transacoes = 0
total_gasto = 0
total_devido = 0
saldo = float(input('Digite seu saldo atual: R$ '))
while True:
    print('===== Lojinha Python =====')
    opcao = int(input('[1] Comprar\n[2] Devolver\n[3] Resumo\n[4] Sair\nDigite um número: '))
#==================== Comprar ======================
    if(opcao == 1):
        while True:
            print('====== Mercado =========')
            opcao_compra = int(input('[1] Seção Frios\n[2] Seção Verduras\n[3] Seção Frutas\n[4] Seção Produtos de Limpeza\n[5] Seção Cosméticos\n[6] Sair\nDigite um número: '))
            if(opcao_compra == 1):
                while True:
                    opcao_frios = int(input('[1] Peixe Tilápia (10.00 R$ 1Kg) \n[2] Coxinha Congelada (R$ 15.00 1kg)\n[3] Pizza Frango com Catupiry Séara (R$ 15.89)\n[4] Voltar\nDigite um número: '))
                    if(opcao_frios == 1):
                        peixe = 10
                        if(peixe <= saldo):
                           saldo -= peixe
                           total_gasto += peixe
                           contador_transacoes += 1
                           print(f'Você comprou 1kg de Peixe e totalizou R${peixe:.2f}' )
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}')
                    elif(opcao_frios == 2):
                        coxinha = 15
                        if(coxinha <= saldo):
                            saldo -= coxinha
                            total_gasto += coxinha
                            contador_transacoes += 1
                            print(f'Você comprou 1kg de Coxinha e totalizou R${coxinha:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}')
                    elif(opcao_frios == 3):
                        pizza = 15.89
                        if(pizza <= saldo):
                            saldo -= pizza
                            total_gasto += pizza
                            contador_transacoes += 1
                            print(f'Você comprou Pizza com Catupiry Seara e totalizou R${pizza:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}')
                    else:
                        break
            elif(opcao_compra == 2):
                while True:
                    opcao_verduras = int(input('[1] 1 Kg Tomate R$ 8.00\n[2] 1 kg Cenoura R$ 4.50\n[3] 1 kg Cebola R$ 5.00\n[4] Voltar\nDigite um número: '))
                    if(opcao_verduras == 1):
                        tomate = 8.00
                        if(tomate <= saldo):
                            saldo -= tomate
                            total_gasto += tomate
                            contador_transacoes += 1
                            print(f'Você comprou tomate e totalizou R${tomate:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}')
                    elif(opcao_verduras == 2):
                        cenoura = 4.50
                        if(cenoura <= saldo):
                            saldo -= cenoura
                            total_gasto += cenoura
                            contador_transacoes += 1
                            print(f'Você comprou cenoura e totalizou R${cenoura:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}')
                    elif(opcao_verduras == 3):
                        cebola = 5.00
                        if(cebola <= saldo):
                            saldo -= cebola
                            total_gasto += cebola
                            contador_transacoes += 1
                            print(f'Você comprou cebola e totalizou R${cebola:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}')
                    else:
                        break








#============================= Devolver ====================
    elif(opcao == 2):
        valor_devolucao = float(input('Digite o valor da devolução: R$ '))
        saldo += valor_devolucao
        total_devido += valor_devolucao
        contador_transacoes += 1
        print(f'Saldo atual: R${saldo:.2f}')
    elif(opcao == 3):
        print(f'Total gasto: R${total_gasto:.2f}')
        print(f'Total devolvido: R${total_devido:.2f}')
        print(f'Quantidade de transações: {contador_transacoes}')
        print(f'Saldo atual: R${saldo:.2f}')
    else:
        break

print('Obrigado por comprar na nossa loja :)')
print('========================')