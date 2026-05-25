alunos = []
conta_alunos = 0
quantidade_alunos = int(input('Quantos alunos tem na turma? '))
while conta_alunos <= quantidade_alunos - 1:
    conta_alunos += 1
    nome_aluno = str(input(f'Nome do aluno {conta_alunos}: '))
    nota_aluno = float(input(f'Nota do aluno {nome_aluno}: '))
    tupla = (nome_aluno, nota_aluno)
    alunos.append(tupla)
print('===== RELATÓRIO =====')
for aluno in alunos:
    nome, nota = aluno
    if(nota >= 7):
        print(f'{nome} - {nota} - Aprovado')
    elif(nota >= 5 and nota < 7):
        print(f'{nome} - {nota} - Recuperação')
    else:
        print(f'{nome} - {nota} -Reprovado')



