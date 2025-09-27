def spiral(n):
    matrix = [[' ']*n for _ in range(n)]
    left, right, top, bottom = 0, n-1, 0, n-1
    char = '#'

    while left <= right and top <= bottom:
        for i in range(left, right+1):
            matrix[top][i] = char
        top += 1
        for i in range(top, bottom+1):
            matrix[i][right] = char
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                matrix[bottom][i] = char
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                matrix[i][left] = char
            left += 1

    for row in matrix:
        print("".join(row))

size = int(input("Enter spiral size (e.g. 15): "))
spiral(size)
