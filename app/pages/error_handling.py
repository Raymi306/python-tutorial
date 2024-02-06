"""25_error_handling.md"""
# pylint: disable=invalid-name
# pylint: disable=bare-except
# pylint: disable=unused-variable
# pylint: disable=import-outside-toplevel
# pylint: disable=disallowed-name


def delta_original():
    """
    >>> delta = delta_original()
    >>> delta(1)
    1.0
    >>> delta(2)
    0.5
    >>> delta(-2)
    0.5
    >>> delta(3.14)
    0.3184713375796178
    >>> delta(0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    >>> delta('foo')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for /: 'int' and 'str'
    """
    # START
    def delta(x):
        return abs(1 / x)
    # END
    return delta


def divide_by_zero_guard():
    """
    >>> delta = divide_by_zero_guard()
    >>> delta(0)
    >>> delta(2)
    0.5
    >>> delta(-2)
    0.5
    """
    # START
    def delta(x):
        if x == 0:
            return None
        return abs(1 / x)
    # END
    return delta


def more_guards():
    """
    >>> delta = more_guards()
    >>> delta(0)
    >>> delta('foo')
    >>> delta(2)
    0.5
    >>> delta(-2)
    0.5
    """
    # START
    def delta(x):
        if x == 0 or not isinstance(x, (float, int)):
            return None
        return abs(1 / x)
    # END
    return delta


def bare_except():
    """
    >>> bare_except()
    That didn't work, let's carry on and try something else
    """
    def delta(x):
        return abs(1 / x)
    # START
    try:
        result = delta(0)
    except:
        print("That didn't work, let's carry on and try something else")
    # END


def nonbare_excepts():
    """
    >>> nonbare_excepts()
    You tried to divide by zero!
    Whoops!
    """
    def delta(x):
        return abs(1 / x)
    # START
    try:
        result = delta(0)
    except ZeroDivisionError:
        print("You tried to divide by zero!")
    except TypeError:
        print("You tried dividing something that is not divisible!")

    # OR

    try:
        result = delta(0)
    except (ZeroDivisionError, TypeError):
        print("Whoops!")
    # END


def control_flow_else():
    """
    >>> control_flow_else()
    Fail
    """
    def delta(x):
        return abs(1 / x)
    # START
    try:
        n = delta(0)
    except:
        print("Fail")
    else:
        print("Success")
    # END


def control_flow_finally():
    """
    >>> import random
    >>> random.seed(4)
    >>> control_flow_finally()
    I only print when no error occurs
    I will print every time
    >>> control_flow_finally()
    I only print when an error occurs
    I will print every time
    """
    import random

    def fail_maybe():
        num = random.randint(0, 1)
        if num == 1:
            raise RuntimeError()

    try:
        fail_maybe()
    except RuntimeError:
        print("I only print when an error occurs")
    else:
        print("I only print when no error occurs")
    finally:
        print("I will print every time")


# pylint: disable=unnecessary-lambda-assignment
def overly_broad_is_bad():
    """
    >>> overly_broad_is_bad()
    About to do task 4
    (2, 0)
    """
    task_1 = task_2 = task_3 = lambda: 0
    task_4 = task_5 = task_6 = cleanup = lambda: 0

    # START
    try:
        task_1()
        task_2()
        task_3()
        print("About to do task 4")
        task_4()
        foo = 2 + task_5()
        cleanup()
        return foo, task_6()
    except:
        print("Something went wrong!")
        return None
    # END


def less_broad():
    """
    >>> less_broad()
    About to do task 4
    (2, 0)
    """
    task_1 = task_2 = task_3 = lambda: 0
    task_4 = task_5 = task_6 = cleanup = lambda: 0
    class TaskError(Exception):
        """pass"""

    # START
    task_1()
    task_2()

    try:
        task_3()
    except TaskError as e:
        print(f"Task 3 failed! {e}")
        return None
    else:
        print("About to do task 4")
        task_4()
        foo = 2 + task_5()
        return foo, task_6()
    finally:
        cleanup()
    # END
# pylint: enable=unnecessary-lambda-assignment


def raise_your_own_1():
    """
    >>> raise_your_own_1()
    """
    def func():
        raise RuntimeError("Optional information goes here")


def raise_your_own_2():
    """
    >>> raise_your_own_2()
    """
    def func(num):
        try:
            return 2 / num
        except ZeroDivisionError as e:
            raise RuntimeError from e


# pylint: disable=missing-class-docstring
def create_your_own():
    """
    >>> create_your_own()
    """
    class MyException(Exception):
        """Raised when the bad thing happens"""

    class MyExceptionChild(MyException):
        pass
# pylint: enable=missing-class-docstring
