while True:
    n = input('Enter the number(n): ')

    if n.isdigit():
        break
    else:
        print('Invalid number')

result = int(n) + int(f'{n}{n}') + int(f'{n}{n}{n}')

print(f'The result of n+nn+nnn is: {result}')
