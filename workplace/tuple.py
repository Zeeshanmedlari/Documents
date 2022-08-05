from re import X


tupleeg = (1,2,3,4)
print(type(tupleeg))
print(tupleeg)

tupleg1 = 1,2,3,4,5,6,1,2,4
print(tupleg1[::4])
print(tupleg1[-4:-1:-1])
print(tupleg1[-4:-7:-1])
print(tupleg1[-4:-1:1])

fruits = ('Apple','Banana','cherries')
#fruits.append('mangoes')
#print(fruits)

fruitsX = list(fruits)
fruitsX.append('mangoes')
fruits = tuple(fruitsX)
print(fruits)

# packing and unpacking

fruitsZ = 'apple','banana','cherries'
(green,yellow,red) = fruitsZ

print(green)
print(yellow)
print(red)