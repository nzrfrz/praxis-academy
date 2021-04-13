tel = {
    'jack': 4098,
    'sape': 4139
}

tel['guido'] = 4127
print(tel)
print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

print()
print("'dict()' contructor builds dictionaries directly from sequences of key-value pair: ")
print(
    dict([('samuel', 4139), ('galiarth', 4127), ('james', 4098)])
)

print()
print("dict comprehensions can be used to create dictionaries from arbitrary key and value expressions: ")
print(
    {x: x ** 2 for x in (2, 4, 6)}
)

print()
print("specify pairs using keyword arguments, when keys are simple strings: ")
print(
    dict(sape=4139, guido=4127, jack=4098)
)
