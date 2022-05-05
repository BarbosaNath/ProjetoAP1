import os
import platform


def clear():
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')


def draw(options, c='X', h='-', v='|') -> None:
    size = len(max(options, key=len))  # Tamanho da maior str da lista
    s = ' '                            # eSpaço vazio para operações com str

    sh = len(str(len(options)))      # Tamanho da
    print(f'{c}{h*(size+sh+5)}{c}')    # s

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

    # X--------X
    # \ 1 - A  \
    # \ 2 - B  \
    # \ ...    \
    # \ n - Z  \
    # X--------X
