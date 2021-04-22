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

print("")
print("Latihan 7. ")
areas = [
    "hallway", 11.25, "kitchen", 18.0,
    "chill zone", 20.0, "bedroom", 10.75,
    "bathroom", 10.50, "poolhouse", 24.5,
    "garage", 15.45
]
del areas[8:9]
print(areas)

print("")
print("Latihan 8. ")
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(S[0:-1:2])

print("")
print("Latihan 9. ")
europe = {'spain': 'madrid', 'france': 'paris',
          'germany': 'berlin', 'norway': 'oslo'}


def getList(dict):
    return dict.keys()


print(getList(europe))

print(europe['france'])

print("")
print("Latihan 10. ")
europe['itali'] = 'rome'

print(europe)
print('itali' in europe)

print("")
print("Latihan 11. ")
europe2 = {'spain': 'madrid', 'france': 'paris',
           'germany': 'bonn', 'norway': 'oslo', 'poland': 'warsaw',
           'australia': 'vienna'}

europe2['germany'] = 'berlin'
europe2.pop('australia')
print(europe)

print("")
print("Latihan 12. ")
country = {
    'spain': {'capital': 'madrid', 'population': 46.77},
    'france': {'capital': 'paris', 'population': 66.03},
    'germany': {'capital': 'berlin', 'population': 80.62},
    'norway': {'capital': 'oslo', 'population': 5.084}
}

print(country['germany']['population'])
country['indonesia'] = {'capital': 'jakarta', 'population': 250}
print(country)

print("")
print("Latihan 13. ")
for x, y in country.items():
    print(f'Ibu Kota {x} adalah', y['capital'])
