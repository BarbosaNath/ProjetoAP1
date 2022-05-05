import Menu

main_menu = ['Admin',
             'Funcionario',
             'Sair'
             ]


cadastro_funcionario_menu = [
    'Ver Lista de Cadastrados',
    'Adicionar Cadastro',
    'Editar Cadastro',
    'Remover Cadastro',
    'Sair']


Menu.clear()
Menu.draw(main_menu)
menu = input(f'Digite uma opção [1-{len(main_menu)}] $ ')

while menu != str(len(main_menu)):
    Menu.clear()
    if menu == '1':
        menu = '0'
        login = ''
        senha = ''
        asterisco = '*'

        while menu != '4':
            Menu.clear()
            Menu.draw([f'Login: {login}',
                       f'Senha: {asterisco*len(senha)}',
                       'Confirmar',
                       'Cancelar'
                       ])
            menu = input('Digite uma opção [1-4] $ ')
            if menu == '1':
                login = input('Digite o Login: ')
            if menu == '2':
                senha = input('Digite a Senha: ')

            if login == 'admin' and senha == 'admin' and menu == '3':
                menu == '0'
                while menu != '5':
                    Menu.clear()
                    Menu.draw(['Cadastrar Funcionario No Banco de Dados',
                               'Remover Funcionario',
                               'Adicionar Nota a Funcionario',
                               'Enviar Nota de Funcionario',
                               'Sair'
                               ])

    if menu == '2':
        menu = '0'
        nome = ''
        idade = ''
        while menu != '4':
            Menu.clear()
            Menu.draw([f'Nome: {nome}',
                       f'Idade: {idade}',
                       'Confirmar',
                       'Cancelar'
                       ])

            menu = input('Digite uma opção [1-4] $ ')
            if menu == '1':
                nome = input('Editar Nome: ')
            elif menu == '2':
                idade = input('Editar Idade: ')

    Menu.clear()
    Menu.draw(main_menu)
    menu = input(f'Digite uma opção [1-{len(main_menu)}] $ ')
