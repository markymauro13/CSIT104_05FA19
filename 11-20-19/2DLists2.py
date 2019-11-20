matrix = []
numberOfRows = int(input("Enter the number of rows: "))
numberOfColumns = int(input("Enter the number of columns: "))

for row in range(0,numberOfRows):
    matrix.append([])   # add an empty new row
    for column in range(0, numberOfColumns):
        value = int(input("Enter an element and press enter: "))
        matrix[row].append(value)

print(matrix)
