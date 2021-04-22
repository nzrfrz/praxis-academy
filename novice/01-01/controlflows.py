### if Statement
# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

## for Statement
### Measure some strings:
# words = ['cat', 'windows', 'defenestrate']
# for w in words:
#     print(w, len(w))


## Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

## Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

# The range() Function
for i in range(5):
    print(i)

print("")

a = ['Mary', 'had', 'a', 'little' 'lamb']
for i in range(len(a)):
    print(i, a[i])

print("")

# Break Continue, and else clause on loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print("")

# Continue statements
# Odd an even numbers
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an odd number", num)
        continue
    print("Found an even number", num)