# create a and b
a = (3, 4)
b = (0, 0)

# create tuple
coordinate = (a, b)

# calculate the distance between 2 points a and b
coordinate_distance = (((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2)) ** 0.5
print(coordinate_distance)
