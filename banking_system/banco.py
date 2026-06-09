print('{:=>5} Banco Python {:=<5}'.format(' ', ' '))
current_statement = 0
total_deposit = 0
total_withdrawal = 0
current_balance = float(input('Saldo atual: R$ '))
while True:
    operation = int(input(f'[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] sair\nEscolha: '))
    # ---------------- DEPOSITO ---------------
    if(operation == 1):
        print('{:=>8} DEPOSITO {:=<8}'.format(' ', ' '))
        deposit = float(input('Valor do deposito: R$'))
        current_balance += deposit
        total_deposit += deposit
        current_statement += 1
        print(f'Deposito realizado! Saldo: R$ {current_balance:.2f}')
        print('{:=>26}'.format(' '))
    # ---------------- SAQUE ---------------
    elif(operation == 2):
        print('{:=>8} SAQUE {:=<8}'.format(' ', ' '))
        withdrawal = float(input('Valor do saque: R$ '))
        if(withdrawal <= current_balance):
           current_balance -= withdrawal
           total_withdrawal += withdrawal
           current_statement += 1
           print(f'Saque realizado! Saldo: R$ {current_balance:.2f}')
        else:
           print(f'Saldo insuficiente: Saldo atual: {current_balance:.2f}')
        print('{:=>26}'.format(' '))

    # ---------------- EXTRATO ---------------
    elif(operation == 3):
        print('{:=>8} Extrato {:=<8}'.format(' ',' '))
        print(f'Saque realizado! - R$ {total_withdrawal:.2f}')
        print(f'Deposito realizado! + R$ {total_deposit:.2f}')
        print('{:->26}'.format(' '))
        print(f'Total de transações: {current_statement}\nSaldo atual: R$ {current_balance:.2f}')
        print('{:=>26}'.format(' '))
    else:
        break