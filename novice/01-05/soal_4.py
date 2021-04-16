print("Latihan 1. ")
a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
print(a[1:-1])

print("")
print("Latihan 2. ")
x = [1.32, 22.1, 2.34]
y = ['1', '13b', 'aa1']
z = [3, 40, 100]
dd = [x, y, z]
print(dd)

print("")
print("Latihan 3. ")
matrix = [
    [5, 9, 8],
    [0, 0, 6]
]
result = [matrix[1][1], matrix[1][2]]
print(result)

print("")
print("Latihan 4. ")
latihan_4 = [0, 5, 2, 10, 4, 9]
print(sorted(latihan_4))
print('Max number is: ', max(latihan_4))

# max_number = latihan_4[0]
# for number in latihan_4:
#     if number > max_number:
#         max_number = number
# print("Largest Number is: ", max_number)

print("")
print("Latihan 5. ")
latihan_5_a = [1, 3, 5]
latihan_5_b = [5, 1, 3]
result_latihan_5 = latihan_5_b + latihan_5_a
print(result_latihan_5)

print("")
print("Latihan 6. ")
latihan_6 = [
    [5, 9, 8],
    [0, 0, 6]
]
change_first_row = latihan_6[0][2] = 10
change_second_row = latihan_6[1][0] = 11
result_latihan_6 = [latihan_6[0], latihan_6[1]]
print(result_latihan_6)