# set is an unordered collection without duplicate items
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print()

print("membership testing: ")
print('orange' in basket)
print('crabgrass' in basket)

print()

# Demonstrate 'set' operations on unique letters
# from 2 words
a = set('abracadabra')
b = set('alacazam')

print("unique letters in 'a': ")
print(a)

print()

print("letters in 'a' but not in 'b': ")
print(a - b)

print()

print("letters in 'a' or 'b' or both: ")
print(a | b)

print()

print("letters in both 'a' and 'b': ")
print(a & b)

print()

print("letters in 'a' or 'b' but not both: ")
print(a ^ b)

print()
# set comprehension
print("'set' also support comprehension: ")
a = {x for x in 'abracadabra' if x not in 'abc'}

print(a)
