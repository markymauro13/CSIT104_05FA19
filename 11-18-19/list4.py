lst = [1,2,3,4,5,6,7,8,9,10]

i = 0
while i <= len(lst)-1:
    print(lst[i])
    i+=1

print(lst[0:5:2])

print(lst[:2])
print(lst[3:])

print(lst[1:-3])
print(lst[-4:-2])

print(lst)  #original
lst[1:3] = [9,8]
print(lst)  #new
