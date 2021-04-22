# Looping Dictionaries
import math
print("create new list while looping: ")
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

print()
print("retrieve key and value at the same time using 'items()': ")
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print()
print("using 'enumerate()' to loop through a sequence with index and calue retrieved at the same time: ")
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print()
print("use 'zip()' to loop over 2 sequences at the same time and pair them: ")
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print()
print("use 'reversed()' to loop sequence in reverse order: ")
for i in reversed(range(1, 10, 2)):
    print(i)

print()
print("use 'sorted()' to loop sequence in sort order: ")
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

print()
print("use 'sorted()' with 'set()' to loop sequence in sort order and eliminate duplicate items: ")
for f in sorted(set(basket)):
    print(f)
