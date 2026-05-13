print('{:=>5} Banco Python {:=<5}'.format(' ', ' '))
extrato_atual = 0
deposito_realizado = 0
saque_realizado = 0
saldo_atual = float(input('Saldo atual: R$ '))
while True:
    operacao = int(input(f'[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] sair\nEscolha: '))
    # ---------------- DEPOSITO ---------------
    if(operacao == 1):
        print('{:=>8} DEPOSITO {:=<8}'.format(' ', ' '))
        deposito = float(input('Valor do deposito: R$'))
        saldo_atual += deposito
        deposito_realizado += deposito
        extrato_atual += 1
        print(f'Deposito realizado! Saldo: R$ {saldo_atual:.2f}')
        print('{:=>26}'.format(' '))
    # ---------------- SAQUE ---------------
    elif(operacao == 2):
        print('{:=>8} SAQUE {:=<8}'.format(' ', ' '))
        saque = float(input('Valor do saque: R$ '))
        saldo_atual -= saque
        saque_realizado += saque
        extrato_atual += 1
        print(f'Saque realizado! Saldo: R$ {saldo_atual:.2f}')
        print('{:=>26}'.format(' '))
    # ---------------- EXTRATO ---------------
    elif(operacao == 3):
        print('{:=>8} Extrato {:=<8}'.format(' ',' '))
        print(f'Saque realizado! - R$ {saque_realizado:.2f}')
        print(f'Deposito realizado! + R$ {deposito_realizado:.2f}')
        print('{:->26}'.format(' '))
        print(f'Total de transações: {extrato_atual}\nSaldo atual: {saldo_atual:.2f}')
        print('{:=>26}'.format(' '))
    else:
        break
