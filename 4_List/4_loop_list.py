"""
a
a b
a b c
a b c d
a b c d e

"""

list = ['a', 'b', 'c', 'd', 'e']
for i in range(0,len(list)+1):
    for j in range(0,i):
        print(list[j], end = ' ')
    print()
