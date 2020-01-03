import math
r = 0

while r is 0:
    try:
        r = abs(float(input('Enter the radius of a circle: ')))
    except ValueError:
        print('Please enter the correct number')

area = math.pi * pow(r, 2)

print(f'r = {r}')
print(f'Area = {area:.2f}')
