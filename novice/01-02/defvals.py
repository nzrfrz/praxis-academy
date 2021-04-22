# Default value only evaluated at function scope
i = 5

def f(arg = i):
    print(arg)

i = 8
f()

print("")

# Passing arguments on subsequent call
def g(a, L = []):
    L.append(a)
    return L

print(g(1))
print(g(2))
print(g(3))

print("")

# Without subsequent call
def h(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

print(h('a'))
print(h(5))
print(h(6))