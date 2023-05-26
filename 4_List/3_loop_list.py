list = [21, 52, 83, 94, 65]
for i in list:
    print(i, end = ' ')
print()
for i in list[:]:
    print(i, end = ' ')
print()
print(list[-1])
for i in range(len(list)-1, -1, -1):
    print("(", i, ",", list[i], ")", end = ' ')
print()
for i, value in enumerate(list):
    print(f'Index: {i}, Value: {value}')