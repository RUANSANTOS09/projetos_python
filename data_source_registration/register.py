class EmptySpaceError(Exception):
    pass

repository_sources = []
while True:
    try:
      menu = int(input('1 - Cadastrar fonte\n2 - Listar fontes\n3 - Buscar fonte\n4 - Remover fonte\n5 - Sair\nDigite uma opção, somente números: '))
    except ValueError:
       print('Opção inválida. Digite apenas números!!!')
    else:
        if (menu == 1):
            def register(name):
                if not name:
                    return 'Erro!! Digite seu nome'
                else:
                    repository_sources.append(name)
                    return name
            try:
                adding_data_source = str(input('Digite o nome da fonte de dados: '))
                if not adding_data_source:
                    raise EmptySpaceError
            except EmptySpaceError:
                print('Espaço em vazio. Tente novamente')
            else:
                register(adding_data_source)
                print('Fonte cadastrada com sucesso!')


        elif (menu == 2):
            def registered_sources(repository_sources):
                return repository_sources
            try:
                display_registered_sources = registered_sources(repository_sources)
                if not display_registered_sources:
                    raise EmptySpaceError
            except EmptySpaceError:
                print('Nenhuma fonte cadastrada')
            else:
                print('Fontes cadastradas:')
                for source in display_registered_sources:
                    print(f'- {source}')

        elif (menu == 3):
            def search_source(search):
                if search in repository_sources:
                    return search


            try:
                searching_source = str(input('Digite o nome da fonte que deseja buscar: '))
                search_results = search_source(searching_source)
                if search_results not in repository_sources:
                    raise ValueError
            except ValueError:
                print('Fonte não encontrada.')
            else:
                print(f'Fonte encontrada: {search_results}')

        elif (menu == 4):
            def remove_source(source):
                return source
            try:
                removing_source = str(input('Digite o nome da fonte que deseja remover: '))
                remove_results = remove_source(removing_source)
                if remove_results not in repository_sources:
                    raise ValueError
            except ValueError:
                print('Fonte não encontrada. Não foi possível remover.')
            else:
                repository_sources.remove(remove_results)
                print('Fonte removida com sucesso.')

        elif (menu == 5):
            print('Encerrando o sistema...')
            break

        else:
            print('Opção Inválida.')














