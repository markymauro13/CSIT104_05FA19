i = 1

while i <= 5:   # while i is less than five do this
    for j in range(1,6):    # prints 1 2 3 4 5, then go back to the while loop and do the next line
        print(j, end =' ')
    print("")   # go down to the next line
    i += 1