user = int(input("Enter your cell number: "))
print("My Cell number is " + str(user))

print()

arr = [

    [0,1,2],
    [3,4,5],
    [6,7,8],

    ]

row = int(input("Enter your row number: "))
col = int(input("Enter your column number: "))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if row == i and col == j:
            print(arr[i][j])


