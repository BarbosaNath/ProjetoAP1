import os
import platform


def clear():
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')


def draw(options, title='', ask=True, cls=True, c='X', h='-', v='|'):
    if cls:
        clear()
    size = len(max(options+[title], key=len))  # Tamanho da maior str da lista
    s = ' '                            # eSpaço vazio para operações com str

    sh = len(str(len(options)))      # Tamanho da
    print(f'{c}{h*(size+sh+5)}{c}')

    if title != '':
        ts = size-len(title)+sh+5
        print(f'{v}{s*(ts//2)}{title}{s*((ts//2) + ts%2)}{v}')
        print(f'{c}{h*(size+sh+5)}{c}')

    for i, option in enumerate(options):
        lo = sh - len(str(i+1))
        sp = size-lo-len(option)

        if len(option) == size:
            print(f'{v} {s*(lo)}{i+1} {h} {option} {v}')
        elif len(options) >= 10:
            if i >= 9:
                print(f'{v} {s*(lo)}{i+1} {h} {option} {s*(sp)}{v}')
            else:
                print(f'{v} {s*(lo)}{i+1} {h} {option} {s*(sp+1)}{v}')
        else:
            print(f'{v} {s*(lo)}{i+1} {h} {option} {s*sp}{v}')

    print(f'{c}{h*(size+sh+5)}{c}')
    if ask:
        return input(f'Digite uma opção [1-{len(options)}] $ ')
    else:
        return

    # X--------X
    # \ 1 - A  \
    # \ 2 - B  \
    # \ ...    \
    # \ n - Z  \
    # X--------X


def draw_line(option, line, options=[], size=0, title='', h='-', v='|',):
    if options != []:
        if size == 0:
            size = len(max(options+[title], key=len))
        sh = len(str(len(options)))
    else:
        sh = len(str(line))

    s = ' '

    lo = sh - len(str(line+1))
    sp = size-lo-len(option)

    if len(option) == size:
        print(f'{v} {s*(lo)}{line+1} {h} {option} {v}')
    elif len(option) >= 10:
        if line >= 9:
            print(f'{v} {s*(lo)}{line+1} {h} {option} {s*(sp)}{v}')
        else:
            print(f'{v} {s*(lo)}{line+1} {h} {option} {s*(sp+1)}{v}')
    else:
        print(f'{v} {s*(lo)}{line+1} {h} {option} {s*sp}{v}')


def fill(options, info):
    new = []
    for i, option in enumerate(options):
        if '{' in option:
            temp = option.split('{')
            temp = temp[-1].strip('}')
            new.append(option.replace(temp, '').format(info[temp]))
        else:
            new.append(options[i])
    return new
