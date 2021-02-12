# функция декоратор
from functools import wraps


def decor(func):
    def inner(*args, **kwargs):
        print('decor.inner start')
        func(*args, **kwargs)
        print('decor.inner end')
    return inner


# Функция для дикорирования
def myFunc(*args, **kwargs):
    print(args[0])


print('-'*40)

# вызов функции до дикорирования
myFunc('hello my func')

print('-'*40)

# декорирование
myFunc = decor(myFunc)


# вызов функции после декарирования
myFunc('hello my func')

# ==============================================#

print('-'*40)


# Функция для дикорирования
def myFunc(*args, **kwargs):
    print(args[0])


# декорирование с переименованием
myFuncDecor = decor(myFunc)

# вызов декорированной функции
myFuncDecor('hello my func')

print('-'*40)


# ===============================================#

# Функция c дикорированием
@decor
def myFunc(*args, **kwargs):
    print(args[0])


# вызов декорированной функции
myFunc('hello my func')


print('-'*40)
# ===============================================#
# двойное декорирование


# Функция для дикорирования
def myFunc(*args, **kwargs):
    print(args[0])


myFunc = decor(myFunc)
myFunc = decor(myFunc)

# вызов декорированной функции
myFunc('hello my func')

print('-'*40)

# или


# Функция c дикорированием
@decor
@decor
def myFunc(*args, **kwargs):
    print(args[0])


myFunc('hello my func')

print('-'*40)


# или
# Функция для дикорирования
def myFunc(*args, **kwargs):
    print(args[0])


# двойное декорирование
myFunc = decor(decor(myFunc))

# вызов декорированной функции
myFunc('hello my func')

print('-'*40)
# ===============================================#


def hello(name):
    return f'Hello, {name}'


def header(func):

    def inner(*args):
        return f'<h1>{func(*args)}</h1>'

    return inner


def divdec(func):

    def inner(*args):
        return f'<dev>{func(*args)}</dev>'

    return inner


hello = divdec(header(hello))

print(hello('world'))


# или
@divdec
@header
def hello(name):
    return f'Hello, {name}'


print(hello('world'))

print('-'*40)
# ===============================================#
# __doc__ and __name__


# Функция для дикорирования
def fun_1(*args, **kwargs):
    """
    doc fun_1
    """
    return args[0]


def decor_1(f):
    def inner(*args):
        return f'<dec>{f(*args)}</dec>'
    inner.__doc__ = f.__doc__
    inner.__name__ = f.__name__
    return inner


fun_1 = decor_1(fun_1)

print(fun_1('hello'))
print('__doc__', fun_1.__doc__)
print('__name__', fun_1.__name__)

print('-'*40)
# ===============================================#
# or


def decor_1(f):
    @wraps(f)
    def inner(*args):
        return f'<dec>{f(*args)}</dec>'
    return inner


@decor_1
def fun_1(*args, **kwargs):
    """
    doc fun_1
    """
    return args[0]


print(fun_1('hello'))
print('__doc__', fun_1.__doc__)
print('__name__', fun_1.__name__)

print('-'*40)
# ===============================================#


def decor_1(f1, f2):

    def inner(*args):
        return f'<dec>{f1(args[0])} {f2(args[1])}</dec>'
    return inner


def fun_1(*args, **kwargs):
    return args[0]


def fun_2(*args, **kwargs):
    return args[0]


fd = decor_1(fun_1, fun_2)

print(fd('hello', 'world'))

print('-'*40)
# ===============================================#
