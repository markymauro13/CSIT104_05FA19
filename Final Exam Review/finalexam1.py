rows,cols = (5,5)
list2d = [[0]*cols] *rows
print(list2d)

print()

sum = 0
for i in range(0,len(list2d)):
    for j in range(0, len(list2d[i])):
        sum += list2d[i][j]

print("Sum is: " + str(sum))

print("--------")

list2d = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    ]
    
total = 0

for column in range(0, len(list2d[0])):
    for row in range(0, len(list2d)):
        total += list2d[row][column]
        print(list2d[column][column])
    print("sum for column " + str(column) + " is " + str(total))
    total = 0
