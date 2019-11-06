# 7

def test(a,b,c,d = 10):
    print(a+b+c+d)
    
test(1,3,4) #defualt d is 10

#test(1, b = 3, c = 4, d = 4)
#test(1, b = 3, 4, d = 4)
#test(a = 1, b = 3, 4, d = 4)
#test(a = 1, b = 3, c = 4, d = 4)
#test(d = 1, b = 3, c = 4, a = 4)


print("---")

def test(num):  # understand global and local variables
    num += 1
    print(num, end = '')


def main():
    test(1)

main()
