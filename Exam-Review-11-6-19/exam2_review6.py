#6

for i in range(1,7):    # controls the numbers of rows
    for j in range(1,i+1):  # controls the numbers on those lines
        print(j, end = '')
    print()


print("------")
        
i = 1

while i <= 6:
    for j in range(1, i+1):
        print(j, end = '')
    print()
    i+=1

print("------")

i = 6

while  i >= 1:  # reversed
    for j in range(1, i+1):
        print(j, end = '')
    print()
    i-=1

