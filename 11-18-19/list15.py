list1 = [1,2,3]
list2 = [4,5,6]

list2 = list1

print(list1)
print(list2)

list1 = [1,2,3]
list2 = [] + list1  # ways to make two lists the same with different memory location
