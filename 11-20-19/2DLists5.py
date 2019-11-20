matrix = [
     [1, 2, 3], [4, 5, 6], [7, 8, 9]
     ]

sum = 0

for column in range(0, len(matrix[0])):
    for row in range(0,len(matrix)):
        sum += matrix[row][column]
    print("Sum for column " + str(column) + " is " + str(sum))

print("- - -")

sum = 0

for row in range(0, len(matrix[0])):
    for column in range(0,len(matrix)):
        sum += matrix[row][column]
    print("Sum for column " + str(column) + " is " + str(sum))
    sum = 0
