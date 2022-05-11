import Menu


def cadastrar():
    asterisco = '*'
    menu = '0'
    cadastro = ['Nome Completo: {nome}',
                'Data de nascimendo: {data_nascimento}',
                'CPF: {cpf}',
                'RG: {rg}',
                'Endereço: {endereco}',
                'Cidade: {cidade}',
                'Bairro: {bairro}',
                'Contato: {telefone}',
                'E-mail: {email}',
                'Estado Civil: {estado_civil}',
                'Confirmar',
                'Cancelar']
    funcionario = {'nome': '',
                   'data_nascimento': '',
                   'cpf': '',
                   'rg': '',
                   'endereco': '',
                   'cidade': '',
                   'bairro': '',
                   'telefone': '',
                   'email': '',
                   'estado_civil': ''}

    while menu != '12':
        menu = Menu.draw(Menu.fill(cadastro, funcionario))
        if menu == '11':
            menu = '0'
            login = ''
            senha = ''
            while menu != '4':
                menu = Menu.draw([
                    f'Defina seu login: {login}',
                    f'Defina sua senha de acesso: {asterisco*len(senha)}',
                    'Confirmar',
                    'Cancelar'
                ], title='Cadastrar Novo Funcionario')
                if menu == '1':
                    login = input('Defina seu login: ')
                if menu == '2':
                    senha = input('Defina sua senha: ')


def login():
    menu = '0'
    login = ''
    senha = ''
    asterisco = '*'

    while menu != '3':
        menu = Menu.draw([f'Login: {login}',
                          f'Senha: {asterisco*len(senha)}',
                          'Confirmar'], title='Login')
        if menu == '1':
            login = input('Digite o Login: ')
        if menu == '2':
            senha = input('Digite a Senha: ')
    return (login, senha)
