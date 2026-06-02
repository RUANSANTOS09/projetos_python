total_team = 0
highlight_of_the_month = ''
more_sales = 0

fixed_goals = (3000,5000)
minimum_goal,ideal_goal = fixed_goals

ana_sales = [1000,1000,1000,2200]
laura_sales = [1000,1000,1100]
pedro_sales = [1000,1400]

seller_data = {
   'Ana': ana_sales,
   'Laura': laura_sales,
   'Pedro': pedro_sales
 }

for name, value in seller_data.items():
    total_sales = sum(value)
    total_team += total_sales
    if(total_sales >= ideal_goal):
        print(f'{name} Vendas realizadas: {len(value)} Total vendido : R${sum(value):.2f} Situação : Bateu a meta ideal')
    elif(total_sales >= minimum_goal):
        print(f'{name} Vendas realizadas: {len(value)} Total vendido : R${sum(value):.2f} Situação : Bateu a meta minima')
    else:
        print(f'{name} Vendas realizadas: {len(value)} Total vendido : R${sum(value):.2f} Situação : Abaixo da meta')

    if (total_sales > more_sales):
        more_sales = total_sales
        highlight_of_the_month = name

average = total_team / len(seller_data)
print(f'Destaque do mês : {highlight_of_the_month} — R${more_sales:.2f}')
print(f'Média da equipe: R${average:.2f}')

