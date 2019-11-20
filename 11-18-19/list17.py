def reverse(lst):
    result = [0]*len(lst)

    for i in range(0, len(lst)):
        result[i] = lst[len(lst)-i-1]   # result[0] = lst[(4)- 0 -1] , 3
                                        # result[1] = lst[(4)- 1 -1] , 2
                                        # result[2] = lst[(4)- 2 -1] , 1
                                        # result[3] = lst[(4)- 3 -1] , 0

    return result



print(reverse([1,2,3,4]))
