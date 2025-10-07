l=float(input("Enter the length of the rectangle: "))
b=float(input("Enter the breadth of the rectangle: "))
area=lambda x,y: x*y
area_of_rectangle=area(l,b)
print(f"The area of the rectangle is: {area_of_rectangle}")