a = 0
b = 1
print(a,b,end = ' ')
for i in range(1,10):
    c = a + b
    print(c,end= ' ')
    a = b 
    b = c