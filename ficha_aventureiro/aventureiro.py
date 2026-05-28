name = str(input('Digite o nome do seu personagem: '))
level = 7
health = 80
health_status = True
mana = 30
unlock_level = level >= 20
attack_checker = health_status and mana > 0
print('{:=>4} Ficha do aventureiro {:=<4}'.format(' ', ' '))
print('Nome: {}\nNível: {}\nVida: {} | Mana: {}\nStatus: {}'.format(name, level, health, mana, health_status))
print('Pode entrar na masmorra? {}\nPode atacar? {}'.format(unlock_level, attack_checker))