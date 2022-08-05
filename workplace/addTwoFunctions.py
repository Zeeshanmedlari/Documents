

def addTwoFuctions1(x,y):
    print(x+y)

addTwoFuctions1(3,4)    
addTwoFuctions1(15,30)
addTwoFuctions1(100,330)
addTwoFuctions1(8.4,7.7)
addTwoFuctions1('Hi',' Zeeshan')


def multiply(x,y):
    result=x*y
    return result
#print((multiply(6,5)))

res = multiply(6,5)
print(res)


print('==================Recursion====================')

def recFunc(n):
    if (n > 0):
        res = n + recFunc(n - 1)
    else:
        res = 0 
    return res

print(recFunc(9))        


print('======================Argument types=====================')

def add(x,y,z):
    print(x+y+z)

add(2,4,6)

def add(x,y,z=10):
    print(x+y+z)
add(2,4,6)    