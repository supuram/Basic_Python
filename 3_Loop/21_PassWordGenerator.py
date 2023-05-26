import random

password = []

num = int(input("How many numbers would you like in your password = "))
symbol = int(input("How many symbols would you like in your password = "))
lettersnum = int(input("How many letters would you like in your password = "))

list_symbol = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','<','>','/']
list_numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ''
for i in range(ord('A'), ord('Z') + 1):
    letters = letters + chr(i) + chr(i + 32)
print(letters)
list_letters = []
for i in range(0,len(letters)):
    list_letters.insert(i,letters[i])
print(list_letters)

for i in range(0,num):
    password.insert(i, random.choice(list_numbers))

for i in range(0,symbol):
    password.insert(i, random.choice(list_symbol))
    
for i in range(0,lettersnum):
    password.insert(i, random.choice(list_letters))

random.shuffle(password)
print(password)
new_password = ""
for i in range(0,len(password)):
    new_password = new_password + password[i]
print("Your password = ",new_password)