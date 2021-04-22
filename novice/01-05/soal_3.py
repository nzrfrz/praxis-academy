# 1. 
string = 'puasa kok laper, eeh ngerti-ngerti ngantuk, butuh kopi !!!'
if type(string) == str:
    print('Yoo langsung ngopi')
else:
    print('Not a string')

boolean = True
if type(boolean) == bool:
    print("That's Right")
else:
    print("Sorry, you wrong !!!")

integer = 45
if type(integer) == int:
    print('It was a number')
else:
    print('Not a number')

print("")

# 2.
high_income = False
good_credit = True
student = True

if high_income and good_credit:
    print('Eligible')
else:
    print('Not Eligible')

if high_income or good_credit:
    print('Eligible')
else:
    print('Not Eligible')

if not student:
    print("Eligible")
else:
    print("Not Eligible")

