a = 5
for i in range(1,a+1):
    b = a
    for j in range(1,i+1):
        b = b-1
    print('  '*b,end = '')
    for j in range(1, i+1):
        print(j,end=' ')
    print()