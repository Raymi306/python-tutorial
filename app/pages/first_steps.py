"""10_first_steps.md"""
from unittest.mock import patch
# pylint: disable=line-too-long
# pylint: disable=redefined-builtin


NONLOCALS = ("patch",)


def hello_world():
    """
    >>> hello_world()
    Hello world
    """
    print('Hello world')


def input_noop():
    """
    >>> input_noop()
    """
    with patch('builtins.input') as input:
        # START
        input()
        # END


def input_and_print(mocked_input_ret):
    """
    >>> input_and_print('hello')
    You typed: hello
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_variable = input()
        print('You typed: ' + my_variable)
        # END


def input_and_print_twice(mocked_input_ret):
    """
    >>> input_and_print_twice('7')
    77
    >>> input_and_print_twice('foo')
    foofoo
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_number = input()
        print(my_number * 2)
        # END


def input_and_print_double_v1(mocked_input_ret):
    """
    >>> input_and_print_double_v1('7')
    14
    >>> input_and_print_double_v1('foo')
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'foo'
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_number = int(input())
        print(my_number * 2)
        # END


def input_and_print_double_v2(mocked_input_ret):
    """
    >>> input_and_print_double_v2('7')
    14
    >>> input_and_print_double_v2('foo')
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'foo'
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_number = input()
        print(int(my_number) * 2)
        # END


def input_and_print_double_v3(mocked_input_ret):
    """
    >>> input_and_print_double_v3('7')
    14
    >>> input_and_print_double_v3('foo')
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'foo'
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        print(int(input()) * 2)
        # END


def input_and_print_double_v4(mocked_input_ret):
    """
    >>> input_and_print_double_v4('7')
    14
    >>> input_and_print_double_v4('foo')
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'foo'
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        my_number = input()
        my_number = int(my_number)
        print(my_number * 2)
        # END


def futures_try_int_input(mocked_input_ret):
    """
    >>> futures_try_int_input(4)
    8
    >>> futures_try_int_input('q')
    That's not a number!
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START

        # preview of the future
        # if we begin a line with a '#', Python will ignore it
        # these lines are called comments
        # they can be useful for documenting important things in your code
        # leaving notes for yourself and others can be very important as you write more code
        # its not uncommon to return to code after just a week away and have no idea where you left off or why...

        my_number_as_string = input()
        try:
            my_number = int(my_number_as_string)
        except ValueError:
            # Python has several builtin error types, knowing when and how
            # to reference the documentation is a valuable skill in its own right
            print('That\'s not a number!')
        else:
            print(my_number * 2)
        # END

def conditions_names(mocked_input_ret):
    """
    >>> conditions_names('Joshua')
    Greetings.  Would you like to play a game?
    >>> conditions_names('Dave')
    I'm sorry, Dave.  I'm afraid I still can't open the podbay doors.
    >>> conditions_names('foobarbaz')
    Hello, foobarbaz
    """
    with patch('builtins.input') as input:
        input.return_value = mocked_input_ret
        # START
        user_input = input('What\'s your name?')
        if user_input == 'Joshua':
            print('Greetings.  Would you like to play a game?')
        elif user_input == 'Dave':
            print("I'm sorry, Dave.  I'm afraid I still can't open the podbay doors.")
        else:
            print('Hello, ' + user_input)
        # END


# pylint: disable=using-constant-test
def conditions_indent():
    """
    >>> conditions_indent()
    True is true...
    You'll see this get printed too!
    """
    if True:
        print('True is true...')
        print('You\'ll see this get printed too!')
# pylint: enable=using-constant-test


def conditions_boolean_logic():
    """
    >>> conditions_boolean_logic()
    At least one var is Foo!
    """

    # Experimenting with conditional logic can be more convenient in the interpreter
    var_1 = 'Foo'
    var_2 = 'Bar'

    if var_1 == 'Foo' and var_2 == 'Foo':
        print('All Foo!')

    if var_1 == 'Foo' or var_2 == 'Foo':
        print('At least one var is Foo!')

    if not var_1 or not var_2:
        print('At least one var is falsey!')


def loops_scream():
    """
    NO TEST
    """
    while True:
        print('hello...', end='')


def loops_input_to_break(mocked_input_se):
    """
    >>> loops_input_to_break(('q',))
    >>> loops_input_to_break(('foo', 'q'))
    You said, foo
    """
    with patch('builtins.input') as input:
        input.side_effect = mocked_input_se
        # START
        while True:
            user_input = input('Type \'q\' to exit')
            if user_input == 'q':
                break
            # An alternate way to format strings, note the f before the lead quote, and the braces around the variable name
            print(f'You said, {user_input}')
        # END


def loops_2_var_counter(mocked_input_se):
    """
    >>> loops_2_var_counter(('q', 'q', 'q'))
    Loopedy loop...
    Loopedy loop...
    Loopedy loop...
    >>> loops_2_var_counter(('q', 'foo', 'q', 'q'))
    Loopedy loop...
    Loopedy loop...
    Loopedy loop...
    Loopedy loop...
    """
    with patch('builtins.input') as input:
        input.side_effect = mocked_input_se
        # START
        counter = 0
        target = 3
        while counter < target:
            val = input(f'You have typed \'q\' {counter} times. Type \'q\' and press enter {target - counter} times to exit.\n')
            if val == 'q':
                counter += 1  # equivalent to `counter = counter + 1`
            print('Loopedy loop...')
        # END


def loops_simple_continue():
    """
    Skip iteration 3 and 7
    >>> loops_simple_continue()
    1
    2
    4
    5
    6
    8
    9
    10
    """
    i = 0
    while i < 10:
        i += 1
        if i in {3, 7}:
            continue
        print(i)


# pylint: disable=import-outside-toplevel
def futures_sock_continue():
    """
    An alternate continue example, with working networking code
    Can play with this by using netcat: nc -l 12345, run program, type into nc stdin
    >>> with patch('time.sleep') as mock_sleep:
    ...     mock_socket_se = ('h', 'i', None)
    ...     mock_sleep.side_effect = RuntimeError('STOP ITERATION FOR TESTING')
    ...     with patch('socket.socket') as mock_socket:
    ...         mock_socket().__enter__().recv.side_effect = mock_socket_se
    ...         try:
    ...             futures_sock_continue()
    ...         except RuntimeError:
    ...             pass
    received h
    received i
    >>> with patch('time.sleep') as mock_sleep:
    ...     mock_socket_se = (None, 'f', None, 'x', None)
    ...     mock_sleep.side_effect = (None, None, RuntimeError('STOP ITERATION FOR TESTING'))
    ...     with patch('socket.socket') as mock_socket:
    ...         mock_socket().__enter__().recv.side_effect = mock_socket_se
    ...         try:
    ...             futures_sock_continue()
    ...         except RuntimeError:
    ...             pass
    received f
    received x
    """
    from time import sleep
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('127.0.0.1', 12345))  # host, port
        sock.setblocking(False)
        while True:
            try:
                data = sock.recv(1)  # unordinarily small receive size for demonstration purposes
            except TimeoutError:
                pass
            if data:
                print(f'received {data}')
                continue
            sleep(0.5)
# pylint: enable=import-outside-toplevel


def collections_item_access():
    """
    >>> collections_item_access()
    3
    foo
    bar
    baz
    ['foo', 'bar']
    ['bar', 'baz']
    foo
    bar
    baz
    2
    value
    42
    key
    13
    value
    42
    key value
    13 42
    """
    # lists
    our_list = ['foo', 'bar', 'baz']
    print(len(our_list)) # 3
    print(our_list[0]) # foo
    print(our_list[1]) # bar
    print(our_list[-1]) # baz
    print(our_list[:2]) # foo, bar - beginning to second element
    print(our_list[1:]) # bar, baz - index 1 to end
    for item in our_list:
        print(item)
    # dictionaries
    our_dict = {'key': 'value', 13: 42}
    print(len(our_dict))
    print(our_dict['key']) # 'value'
    print(our_dict[13]) # 42
    for key in our_dict:
        print(key)
    for value in our_dict.values():
        print(value)
    for key, value in our_dict.items():
        print(key, value)


def collections_instantiations():
    """
    >>> collections_instantiations()
    [1, 2, 3, 4] (1, 2, 3) (1,)
    {1, 2} {'key': 'value', 1: 2}
    ['lorem ipsum', 123456, 'foo bar baz', 7890]
    """
    my_list = [1, 2, 3, 4]
    my_tuple = (1, 2, 3)
    my_tuple_single_item = (1,)  # note the comma here!
    my_dictionary = {'key': 'value', 1: 2}
    my_set = {1, 2}
    my_big_list = [
        'lorem ipsum',
        123456,
        'foo bar baz',
        7890
    ]
    print(my_list, my_tuple, my_tuple_single_item)
    print(my_set, my_dictionary)
    print(my_big_list)


def functions_define():
    """
    >>> functions_define()
    30
    9
    12
    14
    8
    1
    1
    2
    3
    5
    8
    13
    """
    def add_2(num_1, num_2):
        return num_1 + num_2

    def print_collection(collection):
        for item in collection:
            print(item)

    def add_2_default_args(num_1=8, num_2=4):
        return num_1 + num_2

    value_1 = 10
    value_2 = 20
    print(add_2(value_1, value_2)) # 30
    print(add_2(3, 6)) # 9
    print(add_2_default_args()) # 12
    print(add_2_default_args(10)) # 14
    print(add_2_default_args(num_2=0)) # 8
    list_1 = [1, 1, 2, 3, 5, 8, 13]
    print_collection(list_1)


def functions_splat():
    """
    >>> functions_splat()
    Both methods agree; sum of 1, 2, 3, 4 is 10
    (1, 2, 3)
    {'key': 'value', 'foo': 'bar'}
    """
    def sum_4_long_signature(num_1, num_2, num_3, num_4):
        return num_1 + num_2 + num_3 + num_4

    def sum_many(list_nums):
        accumulator = 0
        for num in list_nums:
            accumulator += num
        return accumulator

    # in a function signature, * represents variable positional arguments and will be represented as a tuple.
    # ** represents variable keyword arguments and will be represented as a dictionary
    def varargs(*args, **kwargs):
        print(args)
        print(kwargs)

    my_list = [1, 2, 3, 4]
    result_1 = sum_4_long_signature(*my_list) # splat operator unpacks a list or tuple, double splat (**) unpacks a dictionary
    result_2 = sum_many(my_list)
    if result_1 == result_2:
        print(f'Both methods agree; sum of 1, 2, 3, 4 is {result_1}')

    varargs(1, 2, 3, key='value', foo='bar')
    # (1, 2, 3)
    # {'key': 'value', 'foo': 'bar'}
