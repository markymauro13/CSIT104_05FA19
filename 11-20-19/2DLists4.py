matrix = [
     [1, 2, 3], [4, 5, 6], [7, 8, 9]
     ]

sum = 0

for row in range(0, len(matrix)):
    for column in range(0,len(matrix[row])):
        sum += matrix[row][column]

print("The total is: " + str(sum))
