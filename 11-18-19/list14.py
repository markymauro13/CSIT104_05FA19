#make a list with 10 different numbers given by user

list1=[]

print("Enter 10 numbers, one number per line: ")

for i in range(10):
    print("Index " + str(i) + ': ', end = ' ')
    list1.append(int(input()))

print(list1)
