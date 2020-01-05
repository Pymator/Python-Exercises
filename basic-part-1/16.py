def calculate_difference(number):
    if number > 17:
        return abs((17 - number) * 2)
    else:
        return 17 - number

number = int(input('Enter the number: '))

print(calculate_difference(number))
