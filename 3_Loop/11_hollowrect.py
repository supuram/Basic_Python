row = int(input("Enter the number of rows you want = "))
column = int(input("Enter the number of columns you want = "))
for i in range(1,row+1):
    for j in range(1,column+1):
        if i == 1 or i == row or j == 1 or j == column:
            print("*",end = ' ')
        else:
            print(" ",end = ' ')
    print()