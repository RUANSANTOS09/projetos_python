nome = str(input('Digite o nome do seu personagem: '))
nivel = 7
vida = 80
status_vida = True
mana = 30
desbloquear_nivel = nivel >= 20
verificador_ataque = status_vida and mana > 0
print('{:=>4} Ficha do aventureiro {:=<4}'.format(' ', ' '))
print('Nome: {}\nNível: {}\nVida: {} | Mana: {}\nStatus: {}'.format(nome,nivel, vida, mana, status_vida) )
print('Pode entrar na masmorra? {}\nPode atacar? {}'.format(desbloquear_nivel, verificador_ataque))