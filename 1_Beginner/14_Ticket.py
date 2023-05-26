"""
Ask height. If height is less than 120cm, can't ride. Else they can ride. Now ask their age - If age
is less than 12, charge = 5, age between 12-18 charge = 10, age > 18, charge = 20. Now ask if they
want photos. If yes charge them extra 20, else no extra charge.

"""

height = int(input("Enter your height in cm = "))
bill = 0 
if height < 120:
    print("Sorry, you can't ride")
else:
    age = int(input("Enter your age = "))
    if age < 12:
        print("Tickets for kids are Rs 5 each")
        bill = 5
    elif age > 12 and age < 18:
        print("Tickets for teens are Rs 10 each")
        bill = 10
    else:
        print("Tickets for adults are Rs 20 each")
        bill = 20
    print("Hey do you want photos(Y/N)")
    char = str(input("Enter Y or N = "))
    if char == "Y":
        bill = bill + 20
    print("Total Bill = ",bill)