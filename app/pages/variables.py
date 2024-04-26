# pylint: disable=line-too-long


def variables_assignments():
    """
    >>> variables_assignments()
    4
    4
    """
    # pylint: disable-all
    def foo():
        return 4
    def bar():
        return 5
    def do_something(v1, v2):
        pass
    # pylint: enable-all
    # START
    # assignment as statement
    my_var = foo()
    if my_var:
        print(my_var)
    # assignment as expression, using 'walrus' operator
    # NOTE: The walrus operator only works on Python3.8+
    if my_var := foo():
        print(my_var)

    # a more complicated example
    if (var_1 := foo()) and (var_2 := bar()):
        do_something(var_1, var_2)
    # END


def variables_underscore_as_unused():
    """
    >>> variables_underscore_as_unused()
    hello
    hello
    hello
    """
    # we don't need the numbers in the range, we just want to do an action n times
    for _ in range(3):
        print("hello")

    def returns_two():
        return 3, 'foo'

    # we do not intend to use the first element of the returned tuple
    _, my_var = returns_two()


def variables_scope():
    """
    >>> try:
    ...     variables_scope()
    ... except NameError:
    ...     pass
    2
    """
    var_1 = 2
    def func_1():
        # functions have their own scope
        var_2 = 3

    print(var_1)  # 2
    print(var_2)  # NameError


def variables_block_scope_good():
    """
    >>> variables_block_scope_good()
    100.13
    """
    if True:
        var_1 = 100.13
    else:
        var_1 = -33.12
    print(var_1)  # 100.13


def variables_block_scope_bad():
    """
    >>> try:
    ...     variables_block_scope_bad()
    ... except UnboundLocalError:
    ...     pass
    do something
    """
    if True:
        print("do something")
    else:
        var_1 = True
    print(var_1)  # UnboundLocalError


def runtime_variable_resolution():
    """
    >>> runtime_variable_resolution()
    3
    """
    i = 15
    def foo():
        print(i)
    i = 3
    foo()  # 3


def variables_mutating_outer_scope():
    """
    >>> variables_mutating_outer_scope()
    9.3
    0.0
    9.3
    9.3

    NOTE: THE LAST 9.3 IS INCORRECT.
    Here, global should be nonlocal.
    No pretty way to fix this.
    """
    var_1 = 9.3

    def func_1():
        # accessing variables from an outer scope works fine
        print(var_1)

    func_1()  # 9.3

    def func_2():
        # trying to change them will not work as expected
        var_1 = 0.0
        print(var_1)

    func_2()  # 0.0
    print(var_1)  # 9.3

    def func_3():
        # the global keyword here grants the ability to modify var_1
        global var_1
        var_1 = 'foo'

    func_3()
    print(var_1)  # 'foo'


def variables_nonlocal():
    """
    >>> variables_nonlocal()
    42
    13
    """
    def outer_func():
        var_1 = 42
        def inner_func():
            nonlocal var_1
            var_1 = 13
        print(var_1)  # 42
        inner_func()
        print(var_1)  # 13
    outer_func()


def mutable_objects_no_copy():
    """
    >>> mutable_objects_no_copy()
    [1, 2, 3, 4]
    """
    list_1 = [1, 2, 3]
    list_2 = list_1  # this does not copy the list
    # both variables will reference the same list
    list_1.append(4)
    print(list_2)  # [1, 2, 3, 4]


def mutable_objects_copy():
    """
    >>> mutable_objects_copy()
    [1, 2, 3]
    """
    import copy
    list_1 = [1, 2, 3]
    list_2 = copy.copy(list_1)
    list_1.append(4)
    print(list_2)  # [1, 2, 3]

    # alternatively, you may copy a list with the following syntax:
    list_3 = list_1[:]

    # dictionaries have a copy method, saving you an import
    dict_1 = {1: 2}
    dict_2 = dict_1.copy()
