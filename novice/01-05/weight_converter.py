import math

weight = int(input('Your weight are? '))
units = input("\nON (L)lbs Or (K)kg: ")

def weight_converter(num):
    while type(num) == int:
        if units.upper() == 'L':
            weight_on_pounds = num * 0.45
            print(f'You are {weight_on_pounds} pounds')
        elif units.upper() == 'K':
            weight_on_kilos = num * 0.45
            print(f'You weight are {weight_on_kilos} kilos')
        else:
            print('Only on Kilos or Pounds')
    else:
        print("Please input numbers")


weight_converter(weight)

