error_lines = []
error = 0
logs = [
    'INFO: Sistema iniciado\n',
    'ERRO: Falha ao conectar no banco\n',
    'INFO: Processando arquivo.\n',
    'ERRO: Timeout na requisição\n',
    'INFO: Processamento concluído\n',
    'ERRO: Registro inválido encontrado\n'
]
with open('logs.txt', 'w', encoding='utf-8') as log:
    log.writelines(logs)

with open('logs.txt', 'r', encoding='utf-8') as l:
    f = l.readlines()
    for i, v in enumerate(f, start=1):
        if v.startswith('ERRO:'):
            error_lines.append(f'{i}: {v.rstrip()}\n')
            error += 1
    error_lines.append(f'\nQuantidade de erros: {error}')

with open('errors.txt', 'w', encoding='utf-8') as e:
    e.writelines(error_lines)
    for error in error_lines:
        print(error)




