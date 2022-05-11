import Menu
import Tab


main_menu = ['Admin',
             'Funcionario',
             'Sair']

admin_menu = ['Cadastrar Funcionario No Banco de Dados',
              'Remover Funcionario',
              'Adicionar comentario sobre Funcionario',
              'Enviar Nota de Funcionario',
              'Sair']


menu = '0'
while menu != str(len(main_menu)):
    if menu == '1':
        login, senha = Tab.login()

        if login == 'admin' and senha == 'admin':
            menu == '0'
            while menu != '5':
                menu = Menu.draw(admin_menu)
                if menu == '1':
                    Tab.cadastrar()

    if menu == '2':
        menu = '0'
        idade = ''
        nome = ''
        while menu != '4':
            menu = Menu.draw([f'Nome: {nome}',
                              f'Idade: {idade}',
                              'Confirmar',
                              'Cancelar'
                              ])
            if menu == '1':
                nome = input('Editar Nome: ')
            elif menu == '2':
                idade = input('Editar Idade: ')

    menu = Menu.draw(main_menu, 'Bem Vindo ao SGE')
