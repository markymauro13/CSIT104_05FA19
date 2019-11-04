myList = [1,2,3,4,5,6,7,8,9,10]

for u in myList:
    print(u)
    
print("---")

for i in range(0,len(myList),2):    #exam problem: change to while loop
    print(myList[i])

print("---")

i = 0
while i < len(myList):
    if(i%2==0): 
        print(myList[i])
    i+=1
