list = [34, 56, 89, 97, 63]
for i in list[:]:
    for j in list:
        print(j, end=' ')
    list.remove(i)
    print()

"""
Done by Bing

This will create a copy of list using slicing (list[:]) and iterate over the copy while removing 
elements from the original list using the remove() method.
Using del list[i] in this code will result in an error because i is not an index, but a value in the 
list. The del statement is used to delete elements from a list by index, not by value.
In this code, we are iterating over a copy of the list using slicing (list[:]) and removing elements 
from the original list using the remove() method. The remove() method takes a value as an argument and 
removes the first occurrence of that value from the list.

"""