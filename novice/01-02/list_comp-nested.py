matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print("transpose rows and columns: ")
print(
    [[row[i] for row in matrix] for i in range(4)]
)

print("")

print("nested version of code above with context of 'for' is: ")
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

print("")

print("Full nested loop of code above is: ")
transposed2 = []
for i in range(4):
    transposed2_row = []
    for row in matrix:
        transposed2_row.append(row[i])
    transposed2.append(transposed2_row)

print(transposed2)

print("")
print("Use built-in function 'zip()' to make it more simple: ")
print(
    list(zip(*matrix))
)
