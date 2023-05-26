num = int(input("Enter a number = "))
num1 = num
num_res = num
ct = 0
sum = 0
while num_res/10 != 0:
    num_res = int(num_res / 10)
    ct = ct + 1
while num/10 != 0:
    rem = int(num % 10)
    sum = sum + (rem * 10 ** (ct-1))
    ct = ct -1
    num = int(num / 10)
print(sum)
if sum == num1:
    print("Palindrome")
else:
    print("Not Palindrome")