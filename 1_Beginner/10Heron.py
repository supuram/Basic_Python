side1 = int(input("Enter the length of the first side of a triangle = "))
side2 = int(input("Enter the length of the second side of a triangle = "))
side3 = int(input("Enter the length of the third side of a triangle = "))
if (side1+side2) < side3 or (side1+side3) < side2 or (side2+side3) < side1:
    print("Triangle not possible")
else:
    sum = (side1 + side2 + side3)/2
    print(sum)
    area = sum * (sum - side1) * (sum - side2) * (sum - side3)
    area = area ** 0.5
    print("Area of the triangle = ",area)