def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus", sep=". "))

print()

def parrot(voltage, state='a stiff', action='voom'):
     print("-- This parrot wouldn't", action, end=' ')
     print("if you put", voltage, "volts through it.", end=' ')
     print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

print()

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

print(f(1))

print()

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

print(pairs)

print()

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """

    pass

print(my_function.__doc__)

print()

def i(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", i.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

i('spam')
