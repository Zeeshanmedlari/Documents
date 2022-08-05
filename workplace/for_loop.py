listX = [4,3,2,1]
for i in listX:
    print(i)
    print(i*2)

for l in 'Hello':
    print(l+'*')    

for l in "(Hello World)"+"(New wolrd)":
    print(l[0])

cars = ['Audi','BMW','Tesla','RRR']
for c in cars:
    print(c[0])

carX = ['Audi','BMW','RR','Merc']
for x in carX:
    print(x)
    if x == 'RR':
        break
    print(x)


fruits = ['orange','banana','grapes']
for x in fruits:
    #print(x)
    if x == 'banana':
        continue
    print(x)


for x in range(6):
    #print(x)
    if x == 3: continue
    print(x)

print('============Dict for loop================')

person = {
    'name' : 'Mark',
    'age' : 45,
    'city' : 'Boston'
}

for dictvar in person:
    print(dictvar)

for dictvar in person.keys():
    print(dictvar)

for dictvar in person.values():
    print(dictvar)

for dictvar in person.items():
    print(dictvar)


for char in 'python':
    if char !='o':
        print(char)
        continue
    else: 
        print(char)
        break



