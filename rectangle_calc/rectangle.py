import calculate

length = float (input ("What is the length of the rectangle?: "))
width = float (input("What is the width of the rectangle?: "))


area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f"The area of the rectangle is {area}.")
print(f"The perimeter of the rectangle is {perimeter}.")

