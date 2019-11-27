number = [18,5,36,1,54,12,43,7] # creates list

min_value = max(number)
max_value = 0

for i in number:    # traversing through list
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i
        
print("Result is: " + str(min_value + max_value))   # printing result
    
        
