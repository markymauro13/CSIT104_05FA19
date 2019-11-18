myList = [1,2,3,4,5,6]

for u in myList:
    print(u)

print("---")

for i in range(0,len(myList),2):
    print(myList[i])

print("---")

# prints all odd index items of myList
for u in range(0,len(myList)):
    if u % 2 != 0:
        print(myList[u])
