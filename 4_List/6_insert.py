list = []
n = int(input("Enter the number of elements you want in a list = "))
for i in range(0,n):
    num = int(input("Enter a number you want to insert in the list = "))
    list.insert(i,num)
print(list)