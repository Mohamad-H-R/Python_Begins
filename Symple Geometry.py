# choosing shape for culculating perimeter and area
shape = input("Choose shape (square, rectangle, triangle, circle): ").lower()

# if user chooses square
if shape == "square":
    side1 = float(input("Input side 1: "))
    perimeter = side1 * 4
    area = side1 * side1 
    print(f"Perimeter: {perimeter}\r\nArea:{area}")

# if user chooses rectangle
elif shape == "rectangle":
    side1 = float(input("Input side 1: "))
    side2 = float(input("Input side 2: "))
    perimeter = (side1 + side2) * 2
    area = side1 * side2
    print(f"Perimeter: {perimeter}\r\nArea:{area}")

# if user chooses triangle
elif shape == "triangle":
    side1 = float(input("Input side 1: "))
    side2 = float(input("Input side 2: "))
    side3 = float(input("Input side 3: "))
    base = float(input("Input base: "))
    height = float(input("Input height: "))
    perimeter = side1 + side2 + side3 
    area = base * height / 2
    print(f"Perimeter: {perimeter}\r\nArea:{area}")

# if user chooses circle
elif shape == "circle":
    radius = float(input("Input radius: "))
    perimeter = 2 * radius * 3.14
    area = radius * radius * 3.14
    print(f"Perimeter: {perimeter}\r\nArea:{area}")

# if user chooses anything else
else:
    print("Invalid value, Try again")