ans = 44
print(ans)
array = [1,2,3]
def milk():
    print('open door')
milk()
def add(a,b):   #Here a and b are called parameters
    return a + b
print(add(8,9)) #The value that is being passed to a function when it is called is called argument. Here 8 and 9 are arguments
def pdt(p,q):
    x = 8
    print(x)
    return p**q
print(pdt(p = 3, q = 4))

#Functions that are used with an object/that belong to an object are called methods. Let a car be named kuti.
#Now kuti is an object with attributes like amount of fuel, mileage. The behaviour of kuti is determined by
#its methods like drive().

myAge = 32 #Here myAge is a variable. But 32 is an object. Variables are boxes that hold onto data. The thing
#inside the variable is the actual object. A variable is a way to refer to an object at some point in time. 
