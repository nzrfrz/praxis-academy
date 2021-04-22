t = 12345, 54321, 'hello!'
print(t[0])

print(t)

print("")

print("tuple maybe nested: ")
u = t, (1, 2, 3, 4, 5)

print(u)


print("")

print("can contain mutable objects: ")
v = ([1, 2, 3], [3, 2, 1])

print(v)

print("")

print("Special case: ")
empty = ()
singleton = 'hello',

print("total length in empty: ")
print(len(empty))

print("total length in singleton: ")
print(len(singleton))

print("only singleton: ")
print(singleton)
