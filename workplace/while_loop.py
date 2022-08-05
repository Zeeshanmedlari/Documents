i = 1 
while i < 6:
    #print(i)
    if i == 3:
        break
    i += 1
    print(i)
print('===========================================')
i = 1
while i < 6:
    print(i)
    if i == 3:
        pass
    i += 1
#else: 
    print('i is not longer less than 6')    

print('====================Nested for loop===================')

colours = ['Red','Yellow','Blue']
fruits = ['Apple','Banana','Berries']

for x in colours:
    for y in fruits:
        print(x,y)


for i in range(1,9):
    for j in range(i):
        print(j,end='')
    print()


for i in range('apple'):
    for j in range(i):
        print(i,end='')
    print()
