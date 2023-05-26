list = [34, 56, 89, 97, 63]
k = 0
for i in range(0, len(list)):
    for j in range(0, len(list)):
        print(list[j], end = ' ')
    list.pop(k)
    print()