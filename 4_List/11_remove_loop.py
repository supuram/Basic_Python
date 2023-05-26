list = [34, 56, 89, 97, 63]
for i in range(len(list)-1,-1,-1):
    for j in list:
        print(j, end=' ')
    del list[i]
    print()


"""
Done by Bing

This will iterate over the indices of list in reverse order and delete elements from the list using 
the del statement.

"""