length = input("enter the value for length :")
width = input("enter the value for width :")
if length != width:
    print("Its a square") #its a logical error as the condition itself is wrong and the perimeter is also not calculated correctly
area = length * width
perimeter =  length+width+length # The perimeter is also not calculated correctly
print("The area of the rectangle is :", area)
print("The perimeter of rectangle is :",perimeter)
