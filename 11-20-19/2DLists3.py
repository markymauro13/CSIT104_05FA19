matrix = [
     [1, 2, 3], [4, 5, 6], [7, 8, 9]
     ]
print("  " + str(len(matrix)))
print("- - -")

for row in range(0,len(matrix)):
    for column in range(0, len(matrix[row])):
        print(matrix[row][column], end = " ")
    print()
