arr = []

user = int(input("Enter a number: "))
arr.append(user)

user = int(input("Enter a number: "))
arr.append(user)

user = int(input("Enter a number: "))
arr.append(user)

user = int(input("Enter a number: "))
arr.append(user)

user = int(input("Enter a number: "))
arr.append(user)

print()

inc = 1
for i in range(0,len(arr)):
    if arr[i] >= 0:
        print(str(inc) + ": positive")
    else:
        print(str(inc) + ": negative")
    inc += 1
