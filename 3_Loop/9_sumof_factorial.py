"""
1! + 2! + 3! + 4! + 5! 

"""

num = int(input("Enter a number = "))
sum = 0
for i in range (1,num + 1):
    p = 1
    for j in range (1,i+1):
        p = p * j
    sum = sum + p
print("Result = ", sum)