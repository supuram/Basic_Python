num = int(input("Enter how many numbers you want to add = "))
max = 0
for i in range(num):
    n = int(input("Enter a number = "))
    if n > max:
        max = n
print(max)