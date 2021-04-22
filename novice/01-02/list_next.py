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

print("")
print("Using list as queues: ")

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()


print(queue)

print("")
print("Using list as queues: ")

squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

print("")
print("For one line: ")
print(
    [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
)

print("")
print("For nested loop: ")
combs = []
for x in [2, 3, 4]:
    for y in [3, 4, 5]:
        if x != y:
            combs.append((x, y))

print(combs)