from math import pi
print("using math lib to calculate pi: ")
print(
    [str(round(pi, i)) for i in range(1, 6)]
)

print("")

# Create a list of squares
squares = []
for x in range(10):
    squares.append(x ** 2)

# Creates or overwrite 'x' after loop
squares = list(map(lambda x: x ** 2, range(10)))
# Simple version of code above is below :
squares = [x ** 2 for x in range(10)]

print(squares)

print("")

# Combine 2 lists if they are not equal
print(
    [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
)

# Code above is equal to nested loop below
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)

print("")

# List comprehension contain complex expressions
# and nested functions
vec = [-4, -2, 0, 2, 4]
print("create a new list with the values doubled: ")
print(
    [x * 2 for x in vec]
)

print("")

print("filter the list to exclude negative numbers: ")
print(
    [x for x in vec if x >= 0]
)

print("")

print("apply a function to all the elements: ")
print(
    [abs(x) for x in vec]
)

print("")

print("call a method on each element: ")
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print(
    [weapon.strip() for weapon in freshfruit]
)

print("")

print("create a list of 2-tuples like (number, square): ")
print(
    [(x, x**2) for x in range(6)]
)

print("")
print("flatten a list using a listcomp with two 'for': ")
vec2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(
    [num for elem in vec2 for num in elem]
)
