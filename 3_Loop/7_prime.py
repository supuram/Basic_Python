num = int(input("Enter a number = "))
ct = 0
for i in range(1,num+1):
    if num % i == 0:
        ct = ct + 1
if ct == 2:
    print(num," is prime number")
else:
    print(num," is not a prime number")