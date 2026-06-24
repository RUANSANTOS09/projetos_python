valid = []
customer_valid = 0

invalid = []
customer_invalid = 0
customer = [
    ('  Ana Silva ', 'ana.silva@email.com'),
    ('BRUNO COSTA', 'brunocostaemail.com'),
    (' carla dias', 'carla.dias@email.com'),
    ('Diego Souza  ', 'diegoinvalido'),
    ('eduarda lima', 'eduarda.lima@email.com'),
]
for name,email in customer:
    if '@' in email and '.' in email:
        customer_valid += 1
        valid.append(f'{name.strip().title()} - {email}\n')
    else:
        customer_invalid += 1
        invalid.append(f'{name.strip().title()} - {email}\n')


with open('customer_v.txt', 'w', encoding = 'utf-8') as v:
    v.writelines(valid)
    print(f'Total de clientes válidos: {customer_valid}')


with open('customer_i.txt', 'w', encoding = 'utf-8') as i:
    i.writelines(invalid)
    print(f'Total de clientes invalidos: {customer_invalid}')