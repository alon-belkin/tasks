print('enter a number: ')
x = input()
if x.isnumeric() and len(x) == 3:
    print(x[::-1])
else:
    print(input('enter a 3 digit number: '))

