import sys
for x in sys.argv[1:]:
    if not x.isnumeric() or not len(sys.argv) == 4:
        print('enter 3 numbers')
        exit()
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
if x.isnumeric() and len(sys.argv) == 4:
    x = [a, b, c]
    print(max(x))
    exit()



