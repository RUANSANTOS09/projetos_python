students = []
number_of_students = 0
student_quantity = int(input('Quantos alunos tem na sua turma? '))
while number_of_students <= student_quantity - 1:
    number_of_students += 1
    student_name = str(input(f'Nome do aluno {number_of_students}: '))
    student_note = float(input(f'Nota do aluno {student_name}: '))
    tuple = (student_name, student_note)
    students.append(tuple)
print('===== RELATÓRIO =====')
for student in students:
    name, notes = student
    if(notes >= 7):
        print(f'{name} - {notes} - Aprovado')
    elif(notes >= 5 and notes < 7):
        print(f'{name} - {notes} - Recuperação')
    else:
        print(f'{name} - {notes} -Reprovado')



