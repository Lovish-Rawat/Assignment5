import math
a = float(input("Enter the length of first side: "))
b = float(input("Enter the length of second side: "))
c = float(input("Enter the length of third side: "))
s = (a+b+c)/2
if a+b>=c and b+c>=a and a+c>=b:
    print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
else:
    print("Given triangle is not possible")