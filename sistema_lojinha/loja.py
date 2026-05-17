# ================================================
# Lojinha Python
# Autor: (Ruan)
# Descrição: Sistema de compras no terminal com
#            seções, devoluções e resumo de compras.
# ================================================

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
            print('\n====== Mercado =========')
            opcao_compra = int(input('[1] Seção Frios\n[2] Seção Verduras\n[3] Seção Frutas\n[4] Seção Produtos de Limpeza\n[5] Sair\nDigite um número: '))
            if(opcao_compra == 1):
                print('\n=========== SEÇÃO FRIOS ===========')
                while True:
                    opcao_frios = int(input('[1] Peixe Tilápia (10.00 R$ 1Kg) \n[2] Coxinha Congelada (R$ 15.00 1kg)\n[3] Pizza Frango com Catupiry Séara (R$ 15.89)\n[4] Confirmar e voltar\nDigite um número: '))
                    if(opcao_frios == 1):
                        peixe = 10
                        if(peixe <= saldo):
                           saldo -= peixe
                           total_gasto += peixe
                           contador_transacoes += 1
                           print(f'Você comprou 1kg de Peixe e totalizou R${peixe:.2f}' )
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    elif(opcao_frios == 2):
                        coxinha = 15
                        if(coxinha <= saldo):
                            saldo -= coxinha
                            total_gasto += coxinha
                            contador_transacoes += 1
                            print(f'Você comprou 1kg de Coxinha e totalizou R${coxinha:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    elif(opcao_frios == 3):
                        pizza = 15.89
                        if(pizza <= saldo):
                            saldo -= pizza
                            total_gasto += pizza
                            contador_transacoes += 1
                            print(f'Você comprou Pizza com Catupiry Seara e totalizou R${pizza:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    else:
                        break
            elif(opcao_compra == 2):
                print('\n=========== SEÇÃO VERDURAS ===========')
                while True:
                    opcao_verduras = int(input('[1] 1 Kg Tomate R$ 8.00\n[2] 1 kg Cenoura R$ 4.50\n[3] 1 kg Cebola R$ 5.00\n[4] Confirmar e voltar\nDigite um número: '))
                    if(opcao_verduras == 1):
                        tomate = 8.00
                        if(tomate <= saldo):
                            saldo -= tomate
                            total_gasto += tomate
                            contador_transacoes += 1
                            print(f'Você comprou tomate e totalizou R${tomate:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    elif(opcao_verduras == 2):
                        cenoura = 4.50
                        if(cenoura <= saldo):
                            saldo -= cenoura
                            total_gasto += cenoura
                            contador_transacoes += 1
                            print(f'Você comprou cenoura e totalizou R${cenoura:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    elif(opcao_verduras == 3):
                        cebola = 5.00
                        if(cebola <= saldo):
                            saldo -= cebola
                            total_gasto += cebola
                            contador_transacoes += 1
                            print(f'Você comprou cebola e totalizou R${cebola:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    else:
                        break
            elif(opcao_compra == 3):
                while True:
                    print('\n=========== SEÇÃO FRUTAS ===========')
                    opcao_frutas = int(input(f'[1] Banana Prata R$ 6.00\n[2] Laranja Pêra R$ 5.00\n[3] Maçã Nacional R$ 10.00\n[4] Confirmar e voltar\nDigite um número: '))
                    if(opcao_frutas == 1):
                        banana = 6.00
                        if(banana <= saldo):
                            saldo -= banana
                            total_gasto += banana
                            contador_transacoes += 1
                            print(f'Você comprou banana e totalizou R${banana:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    elif(opcao_frutas == 2):
                        laranja = 5.00
                        if(laranja <= saldo):
                            saldo -= laranja
                            total_gasto += laranja
                            contador_transacoes += 1
                            print(f'Você comprou laranja e totalizou R${laranja:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    elif(opcao_frutas == 3):
                        maca = 10.00
                        if(maca <= saldo):
                            saldo -= maca
                            total_gasto += maca
                            contador_transacoes += 1
                            print(f'Você comprou maçã e totalizou R${maca:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    else:
                        break
            elif(opcao_compra == 4):
                while True:
                    print('\n=========== SEÇÃO PRODUTOS DE LIMPEZA ===========')
                    opcao_limpeza = int(input('[1] Detergente (500ml) R$ 4.50\n[2] Sabão em pó 1kg R$ 10.00\n[3] Amaciante de Roupas (2L) R$10.00\n[4] Confirmar e voltar\nDigite um número: '))
                    if(opcao_limpeza == 1):
                        detergente = 4.50
                        if(detergente <= saldo):
                            saldo -= detergente
                            total_gasto += detergente
                            contador_transacoes += 1
                            print(f'Você comprou detergente e totalizou R${detergente:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    elif(opcao_limpeza == 2):
                        sabao = 10.00
                        if(sabao <= saldo):
                          saldo -= sabao
                          total_gasto += sabao
                          contador_transacoes += 1
                          print(f'Você comprou sabao e totalizou R${sabao:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')

                    elif(opcao_limpeza == 3):
                        amaciante = 10.00
                        if(amaciante <= saldo):
                          saldo -= amaciante
                          total_gasto += amaciante
                          contador_transacoes += 1
                          print(f'Você comprou amaciante de roupas e totalizou R${amaciante:.2f}')
                        else:
                            print(f'SEU SALDO É R${saldo:.2f} SALDO INSUFICIENTE')
                        print(f'Saldo atual: R${saldo:.2f}\n')
                    else:
                        break
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