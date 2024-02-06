"""23_classes.md"""
# pylint: disable=line-too-long
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=unused-variable
# pylint: disable=import-outside-toplevel


def first_class():
    """
    >>> MyType = first_class()
    >>> MyType.class_attribute
    0
    >>> MyType.regular_attribute
    Traceback (most recent call last):
        ...
    AttributeError: type object 'MyType' has no attribute 'regular_attribute'
    >>> instance_1 = MyType(42)
    >>> instance_1.instance, instance_1.class_attribute
    (1, 1)
    >>> MyType.class_attribute
    1
    >>> instance_1.regular_attribute
    42
    >>> instance_1.regular_attribute = -700
    >>> instance_1.regular_attribute
    -700
    >>> instance_2 = MyType(13)
    >>> instance_2.instance, instance_2.class_attribute
    (2, 2)
    >>> instance_1.my_method()
    Instance: 1, Regular Attribute: -700
    >>> instance_2.regular_attribute
    13
    """
    # START
    class MyType:
        class_attribute = 0
        def __init__(self, arg):
            self.regular_attribute = arg
            MyType.class_attribute += 1
            self.instance = MyType.class_attribute

        def my_method(self):
            print(f"Instance: {self.instance}, Regular Attribute: {self.regular_attribute}")
    # END
    return MyType


def person_class():
    """
    >>> Person = person_class()
    >>> person_1 = Person("Bill", 33)
    >>> person_2 = Person(name="Jill", age=44)
    >>> person_1.name, person_1.age
    ('Bill', 33)
    >>> person_2.name, person_2.age
    ('Jill', 44)
    >>> person_1.greet(person_2)
    Hello, Jill, my name is Bill!
    >>> person_1.birthday()
    >>> person_1.age
    34
    """
    # START
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self, person):
            print(f'Hello, {person.name}, my name is {self.name}!')

        def birthday(self):
            self.age += 1
    # END
    return Person


def class_dunder_eq():
    """
    >>> Foo = class_dunder_eq()
    >>> f1 = Foo(13)
    >>> f2 = Foo(42)
    >>> f3 = Foo(13)
    >>> f4 = f3
    >>> f1 == f2
    False
    >>> f1 == f3
    True
    >>> f1 is f3
    False
    >>> f3 is f4
    True
    """
    # START
    class Foo:
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other.value
    # END
    return Foo


def callable_type():
    """
    >>> CallableType = callable_type()
    >>> c = CallableType()
    >>> c()
    You rang?
    """
    # START
    class CallableType:
        def __call__(self):
            print("You rang?")
    # END
    return CallableType


def context_manager_type():
    """
    >>> ContextManagerType = context_manager_type()
    >>> c = ContextManagerType()
    >>> with c as bound_var:
    ...     print(bound_var)
    setup! here's a foo!
    foo
    cleanup!
    """
    # START
    class ContextManagerType:
        def __enter__(self):
            print("setup! here's a foo!")
            return "foo"
        def __exit__(self, *args, **kwargs):
            print("cleanup!")
    # END
    return ContextManagerType


def enum_ints():
    """
    >>> StoplightColors = enum_ints()
    >>> StoplightColors.YELLOW
    <StoplightColors.YELLOW: 2>
    >>> StoplightColors.YELLOW.value
    2
    """
    # START
    from enum import Enum

    # The below syntax represents inheritance
    # This means that our class StoplightColors has all of the properties
    # of the Enum class
    class StoplightColors(Enum):
        # You must assign an integer to each enumerated value
        GREEN = 1
        YELLOW = 2
        RED = 3
    # END
    return StoplightColors

def enum_str():
    """
    >>> StoplightColors = enum_str()
    >>> StoplightColors.GREEN
    <StoplightColors.GREEN: 'green'>
    >>> StoplightColors.GREEN.value
    'green'
    """
    from enum import Enum
    # START
    # The below syntax represents multiple inheritance
    # This gives the properties of both str and Enum to our class
    # This may be useful if we want to retrieve a string value instead of an integer value
    # Python 3.11 adds a StrEnum class that you can import that gives this functionality with a few extra features.
    class StoplightColors(str, Enum):
        GREEN = 'green'
        YELLOW = 'yellow'
        RED = 'red'
    # END
    return StoplightColors


def dataclasses():
    """
    >>> dataclasses()
    """
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str
        age: int = 0
