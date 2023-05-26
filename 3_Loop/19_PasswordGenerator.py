import random

password = ""

num = int(input("How many numbers would you like in your password = "))
symbol = int(input("How many symbols would you like in your password = "))
lettersnum = int(input("How many letters would you like in your password = "))

list_symbol = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','<','>','/']
letters = ''
for i in range(ord('A'), ord('Z') + 1):
    letters = letters + chr(i) + chr(i + 32)
print(letters)
list_letters = []
for i in range(0,len(letters)):
    list_letters.insert(i,letters[i])
print(list_letters)

for i in range(0,num):
    randnum = random.randint(0,9)
    password = password + str(randnum)

for i in range(0,symbol):
    password = password + random.choice(list_symbol)
    
for i in range(0,lettersnum):
    password = password + random.choice(list_letters)

print(password)