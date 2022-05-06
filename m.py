import Menu

class Funcionario:
    def __init__(self) -> None:
        self.nome: str
        self.data_nascimento: str
        self.cpf: str
        self.rg: str
        self.endereco: str
        self.cidade: str
        self.bairro: str
        self.telefone: str
        self.email: str
        self.estado_civil: str

main_menu = ['Admin',
             'Funcionario',
             'Sair'
             ]

admin_menu = ['Cadastrar Funcionario No Banco de Dados',
              'Remover Funcionario',
              'Adicionar comentario sobre Funcionario',
              'Enviar Nota de Funcionario',
              'Sair']


Menu.clear()
Menu.draw(main_menu, 'Bem Vindo ao Sistema')
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
                    Menu.draw(admin_menu)
                    menu = input('Digite uma opção [1-5] $ ')

                    if menu == '1':
                        menu = '0'
                        nome = ''
                        data_nascimento = ''
                        cpf = ''
                        rg = ''
                        endereco = ''
                        cidade = ''
                        bairro = ''
                        telefone = ''
                        email = ''
                        estado_civil = ''
                        while menu != '12':
                            Menu.draw([f'Nome Completo: {nome}',
                                       f'Data de nascimendo: {data_nascimento}',
                                       f'CPF: {cpf}',
                                       f'RG: {rg}',
                                       f'Endereço: {endereco}',
                                       f'Cidade: {cidade}',
                                       f'Bairro: {bairro}',
                                       f'Contato: {telefone}',
                                       f'E-mail: {email}',
                                       f'Estado Civil: {estado_civil}',
                                       f'Confirmar',
                                       f'Cancelar'
                                       ])

                            menu = input('Digite uma opção [1-5] $ ')
                            if menu == '11':
                                menu = '0'
                                login = ''
                                senha = ''
                                while menu != '4':
                                    Menu.draw([f'Defina seu Login: {login}',
                                               f'Defina sua senha de acesso: {senha}',
                                               f'Confirmar',
                                               f'Cancelar'], title='Cadastrar Novo Funcionario')
                                    menu = input('Digite uma opção [1-4] $ ')
                                    if menu == '1':
                                        login = input('Defina seu login: ')
                                    if menu == '2':
                                        senha = input('Defina sua senha: ')

    if menu == '2':
        menu = '0'
        login = ''
        idade = ''
        nome = ''
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
    Menu.draw(main_menu, 'Bem Vindo ao Sistema')
    menu = input(f'Digite uma opção [1-{len(main_menu)}] $ ')
