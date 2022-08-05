'''def add(x,y,z=10):
    print(x+y+z)
add(8,9,)'''

from dis import dis


def add(x,z,y=10):
    print(x+y+z)
add(8,9,)    

print("==================variable arguments =================")

def displayStudentsNames(*names):
    print(names)
displayStudentsNames('Prajwal','Ankit','Ravit','Mustafa') 

print("==================keyword arguments =================")

def person(**personData):
    print(personData)
person(name='john', age=45)


print("==================function arguments =================")
def  allArgsParams(name,*language,country='USA',**bookAuthors):
    print(name,country,language,bookAuthors)
allArgsParams('john','English','French','Spanish','Italian',book1='author1',book2='author2',book3='author3',book='author4')
