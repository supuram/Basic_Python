num = int(input("Enter a number = "))
sum = 0
ct = 0
while num/10 != 0:
    rem = num % 10
    sum = sum + int(rem)
    print(num)
    ct = ct + 1
    num = int(num /10)
print("Number of digits in the number = ",ct)
print("Sum of digits of a number = ",sum)