squares = [1, 4, 9, 16, 25]
print(squares)
print()

print("Print first index of square lists: ")
print(squares[0])

print("Print last index of square lists: ")
print(squares[-1])

print("Print Last 3 index of squares list: ")
print(squares[-3:])

print("Add new lists to square list: ")
print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
cubes[3] = 4 ** 3
print(cubes)

print("Add cubes of 6")
cubes.append(6 ** 3)
cubes.append(7 ** 3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Replace values: ")
letters[2:5] = ['C', 'D', 'E']
print('Remove them: ')
letters[2:4] = []
print(letters)

print("")

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b

print("")

i = 256 * 256
print('The value of i is: ', i)

x, y = 0, 1
while x < 100:
    print(x, end=',')
    x, y = y, x + y