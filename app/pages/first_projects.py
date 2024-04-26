"""11_first_projects.md"""
from unittest.mock import patch
# pylint: disable=line-too-long
# pylint: disable=redefined-builtin
# pylint: disable=import-outside-toplevel


NONLOCALS = ("patch",)


def random_numbers():
    """
    >>> import random
    >>> random.seed(1)
    >>> random_numbers()
    18
    73
    98
    9
    33
    16
    64
    98
    58
    61
    """
    import random

    for _ in range(10):
        print(random.randint(1, 100))


def guessing_game(mocked_input_se):
    """
    >>> import random
    >>> random.seed(1)
    >>> guessing_game(('y', '18', 'y', '1', 'n'))
    You win!
    You lose!
    Game over!
    """
    with patch('builtins.input') as input:
        input.side_effect = mocked_input_se
        # START
        from random import randint

        while input('Play game? y/n: ') == 'y':
            answer = randint(1, 100)
            guess = int(input('Guess a number between 1 and 100: ').strip())
            if guess == answer:
                print('You win!')
            else:
                print('You lose!')
        print('Game over!')
        # END


# pylint: disable=redefined-outer-name
def argv():
    """
    >>> import sys
    >>> sys.argv = 'codeblocks.py', 'foo', 'bar'
    >>> argv()
    ('codeblocks.py', 'foo', 'bar')
    codeblocks.py
    foo bar
    """
    from sys import argv
    print(argv) # prints all args
    print(argv[0]) # is always the name of the program
    # caution!
    # the below line will fail if at least 2 arguments aren't passed in to the program!
    print(argv[1], argv[2])
# pylint: enable=redefined-outer-name


def file_io():
    """no tests, was run manually"""
    with open('my_file.txt', 'w', encoding='ascii') as f: # second argument is the mode to open the file in, w is for write
        # encoding above refers to how bytes translates to characters.
        # ascii is very common for simple english text and special characters.
        # utf-8 covers characters from many languages, and even emojis
        # character encodings are an interesting topic for further reading if you're curious
        f.write('This is both the beginning\nand the end\n')

    with open('my_file.txt', 'a', encoding='ascii') as f: # a is for append
        f.write('This is the new end\n')

    with open('my_file.txt', 'r', encoding='ascii') as f: # r for read
        for i, line in enumerate(f):
            print(f'line {i}: {line}', end='') # we can tell print not to add a new line at the end
            # we already have new lines on the lines we are reading

    with open('my_file.txt', 'r+', encoding='ascii') as f: # r+ for read and write
        f.seek(17) # advance forward in the file 17 characters
        f.write('foobarbaz')
        f.seek(0) # back to the beginning!
        print(f.readline()) # let's see the result


# pylint: disable=import-error
def imports_1():
    """no tests"""
    import example_b
    # variables and functions defined inside of example_b can be accessed like so:
    example_b.some_function()


def requests_demo():
    """no tests"""
    import requests
    response = requests.get('http://example.com')
    print(response.text)


def soup_demo():
    """no tests"""
    from bs4 import BeautifulSoup
    import requests
    response = requests.get('http://example.com')
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    headers = soup.find_all('h1')
    print(headers[0].text)
# pylint: enable=import-error
