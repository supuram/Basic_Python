list = ['apple', 'banana', 'jackfruit', 'kiwi', 'lily']
newlist = []
k = 0
for i in list:
    if 'a' in i:
        newlist.insert(k, i)
        k = k + 1
print(newlist)