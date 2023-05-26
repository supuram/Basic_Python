"""
In a restaurant order 
rice - 100. 
Chicken - 150(3 pieces). 
Extra masala needed - 30. 
Dessert - 50. 

"""

cost = 0
print("Do you want rice")
rice = str(input("Enter Y or N = "))
if rice == "Y":
    cost = cost + 100
print("Do you want chicken")
chicken = str(input("Enter Y or N = "))
if chicken == "Y":
    cost = cost + 150
print("Do you want extra masala")
masala = str(input("Enter Y or N = "))
if masala == "Y":
    cost = cost + 30
print("Do you want dessert")
dessert = str(input("Enter Y or N = "))
if dessert == "Y":
    cost = cost + 50
print("The total cost = ",cost)
