import math
from fractions import Fraction

r = 6
volume = Fraction(4, 3) * math.pi * pow(r, 3)

print(f'The volume of a sphere with radius {r} is {volume:.2f}')
