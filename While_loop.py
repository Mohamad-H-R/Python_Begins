
n = int(input("Choose your number: "))

print(n, end=" ")

while n != 1:
    if n % 2 == 0:   
        n = n // 2
    else:            
        n = 3 * n + 1
    
    print(n, end=" ")
