from logging.config import listen
from re import L


names= ['Ankit','Raviteja','Aafreen','Pawan','Vinod']
print(names)
print(names[::-1])

listEg= ['John',45,18.98]
print(type(listEg))
print(listEg[0][2])

listeg1= ['john',45,18.98,['French','spanish','English']]
print(listeg1[3][1][3])

listeg2= ['john',45,18.98,['French','Spanish','English',('python','C','C++')]]
print(type(listeg2))
print(listeg2[3][3][0][3])

listeg3 = [1,2,3,4]
listeg3.append(5)
print(listeg3)

var2 = listeg3

print(var2)

listeg3[2]=5
print(listeg3)

listeg3.sort
print(listeg3)

listeg3.reverse
print(listeg3)


listeg4 = [6,7,8,9,11,15,17,20]
listeg4.reverse()
print(listeg4)
