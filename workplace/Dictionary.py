from heapq import merge
from this import d


dictx = {
    'Brand' : 'Audi',
    'Model' :  'q5',
    'year'  :  '2015'

}

print(dictx)
print(type(dictx))

print(dictx['Model'])

dict1 = {
    (1,2,3) : 'First',
    2 : 22,
    3 : 33
}
print(dict1)
print(dict1[(1,2,3)][2])
print(type(dict1))


a= (1,2,3,4,5)
b= 'Ankit'
dict2 = {
    a : 'v1',
    b : 'V2'
}

print(dict2)


se = {
    'id' : 45678,\
    'name' : 'john',\
    'Height' : 6.5,\
    'Languages' : ['English','Hindi','Spanish','Italian',['C','C++','Python']],\
    'Adress' : ('Residentail','Permanent'),\
    'male': True,\
    'Education' : {'UG','PG'}\
}

print(se)
print(se['Languages'][4][2][3])
print(se.items())


listx = [(0,'zero'),(1,'one')]
print(type(listx))
newdict= dict(listx)
print(newdict)
print(type(newdict))


tuple3 = ([0,'zero'],[1,'one'])
print(tuple3)
print(type(tuple3))
dictex = dict(tuple3)
print(dictex)
print(type(dictex))


dictm = {
    1 : 11,
    2 : 22,
    3 : 33,
}

dictn = {
    4 : 44,
    5 : 55,
    6 : 66,
}

print(dictm.pop(3))
print(dictm)

# Nested Dictionary

print('=================one way===================')

Family1 = {
        'C1' : {
            'Name' : 'John',
            'Age': 36,
            },
        'C2' : {
            'Name' : 'Mark',
            'Age' : 50,
        },
        'C3' : {
            'Name' : 'Ankit',
            'Age' : 46,
        }    
} 

print(Family1)

print('==============Another Way===============')

C1 = {
    'Name' : 'John',
    'Age' : 36,
}
C2 = {
    'Name' : 'Mark',
    'Age' : 50,
}
C3= {
    'NAme' : 'Ankit',
    'Age' : 46,
}

Family2 = {
    'c1' : C1,
    'c2' : C2,
    'c3' : C3
}
print(Family2)