import random
str = "apple,orange,banana,jackfruit"
list = str.split(",")
print(list)
for i in range(0,len(list)):
    rand_int = random.randint(0, len(list)-1)
    print(list[rand_int],end = ' ')
