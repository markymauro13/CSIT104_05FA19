list1 = [1,2,3,4,5,5,7,3,6]
list1.append(20)

print(list1)

print(list1.count(7))
print(list1.count(5))

list2 = [0,9]
list1.extend(list2)
print(list1)

print(list1.index(5))

list1.insert(1,25)
print(list1)
