# Fizz Buzz exercise
# Have a function that take an input
# Depend on input, if given input is 3 will return string 'Fizz'
# if given input is 5 will return 'Buzz'
# if given input is division by 3 and 5 will return 'Fizz Buzz'
# if given input are other than that return 'same value' from the input

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


num = int(input('Enter number: '))
print(fizz_buzz(num))