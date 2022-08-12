from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from string import punctuation
from random import choice
from random import choice
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.progress import track
from time import sleep
# COUNTER = 0
console = Console()
chars = ''

console.print(Panel('''It includes a smart setting for the length of the password,
as well as what characters you want to include in it,
and which ones to exclude.''', title='[blue]Password generator'), justify='center')


def app():
    characteristis()


def characteristis():
    console.print(Panel('[blue]How long is the password you want?[/blue]'))
    length = int(input(' enter: '))
    # console.print(Panel('[blue]How many passwords do you need to generate?[/blue]'))
    # how = int(input(' enter: '))
    setup(chars, length)


def setup(chars, length):
    match console.input('-- Would you like to include [blue]numbers[/blue]? --\n'):
        case '+':
            chars += digits
    match console.input('-- Would you like to include [blue]uppercase[/blue] letters? --\n'):
        case '+':
            chars += ascii_uppercase
    match console.input('-- Would you like to include [blue]lowercase[/blue] letters?  --\n'):
        case '+':
            chars += ascii_lowercase
    match console.input('-- Would you like to include [blue]punctuation?[/blue] --\n'):
        case '+':
            chars += punctuation
    match console.input('-- Would you like to exclude [blue]ambiguous characters[/blue] il1Lo0O --\n'):
        case '+':
            for symbols in 'il1Lo0O':
                chars += chars.replace(symbols, '')

    generate(chars, length)


def generate(chars, length):
    new_password = ''
    for _ in range(length):
        new_password += choice(chars)
    console.print(Panel(f'Your password is [blue]{new_password}[/blue]',
title='[blue]Password generator'))


# for _ in range(how):
#     generate(chars, length, how)
#     COUNTER += 1
#     for _ in track(range(50), description='[blue]Processing...'):
#         sleep(0.03)
#         console.print(Panel(f'Your [red]{COUNTER}[/red] password is [blue]{new_password}[/blue]',
# title='[blue]Password generator'))
#     print('-- [red]Would you like to repeat it?[/red] -- ')
#     match input('here: '):
#         case '+':
#             app()


if __name__ == '__main__':
    app()
