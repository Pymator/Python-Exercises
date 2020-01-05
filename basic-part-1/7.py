import os

filename = ''

while filename == '':
    filename = input('Enter the filename: ')

# Method 1
extension = filename.split('.')[-1]
print(extension)

# Method 2
extension1 = os.path.splitext(filename)
print(extension1[-1].lstrip('.'))
