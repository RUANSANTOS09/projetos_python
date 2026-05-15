contador_transacoes = 0
total_gasto = 0
total_devido = 0
saldo = float(input('Digite seu saldo atual: R$ '))
while True:
    print('===== Lojinha Python =====')
    opcao = int(input('[1] Comprar\n[2] Devolver\n[3] Resumo\n[4] Sair\nDigite um número: '))
#==================== Comprar ======================
    if(opcao == 1):
        valor_compra = float(input('Digite o valor da sua compra: R$ '))
        if(valor_compra <= saldo):
           saldo -= valor_compra
           total_gasto += valor_compra
           contador_transacoes += 1
           print(f'Compra Efetuada!!!')
        else:
            print('Saldo Insuficiente')
        print(f'Saldo atual: R${saldo:.2f}')
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
