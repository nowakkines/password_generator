from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from string import punctuation
from random import choice

CHARS = ''

def hello():
    ''

def setup():
    global chars
    match console.input('-- Would you like to include [blue]numbers[/blue]? (+) --\n'):
        case '+':
            chars += digits
    match console.input('-- Would you like to include [blue]uppercase[/blue] letters? (+) --\n'):
        case '+':
            chars += ascii_lowercase
    match console.input('-- Would you like to include [blue]lowercase[/blue] letters? (+) --\n'):
        case '+':
            chars += ascii_lowercase
    match console.input('-- Would you like to include [blue]punctuation?[/blue] (+) --\n'):
        case '+':
            chars += punctuation
    match console.input('-- Would you like to exclude [blue]ambiguous characters il1Lo0O[/blue] (+) --\n'):
        case '+':
            for symbols in 'il1Lo0O':
                chars += chars.replace(symbols, '')
    print(generate(length, chars))


def generate(length, chars):
    new_password = ''
    for _ in range(length):
        new_password += choice(chars)
    return console.print(Panel(f'Your password is [blue]{new_password}[/blue]',
    title='[blue]Password generator'), justify='center')


# def result():
#     pass


def generate():
    pass

def result():
    pass