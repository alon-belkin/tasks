print('enter a 3 digit number: ')
x = input()
if x.isnumeric() and len(x) == 3:
    print(x[::-1])
else:
    print('input should be a 3 digit number')

