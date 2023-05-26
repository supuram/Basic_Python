"""

        1 
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

"""

for i in range(1,6):
    k=1
    for j in range(1,6):
        if((i+j)>5):
            print(k, end = ' ')
            k = k + 1
        else:
            print(" ", end = ' ')
    print()

   