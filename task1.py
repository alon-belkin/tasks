import sys

if not len(sys.argv) == 3:
    print('enter 2 numbers')
    exit()

if not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
    print('arguments should be a number')
    exit()

a = int(sys.argv[1])
b = int(sys.argv[2])
c = a + b
print(c)
