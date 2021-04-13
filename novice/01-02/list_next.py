fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana', 5))

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)

print("")
print("Using list as stack: ")

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

