import math

weight = int(input('Your weight are? '))


def weight_converter(num):
    if type(num) == int:
        print(type(num))
        # units = input("\nON (L)lbs Or (K)kg: ")
        # if units.upper() == 'L':
        #     weight_on_pounds = num * 0.45
        #     print(f'You are {weight_on_pounds} pounds')
        #     break
        # elif units.upper() == 'K':
        #     weight_on_kilos = num * 0.45
        #     print(f'You weight are {weight_on_kilos} kilos')
        #     break
        # else:
        #     print('Only on Kilos or Pounds')
        #     break
    else:
        print("Please input numbers")


weight_converter(weight)
