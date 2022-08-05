# ways of writting strings

name="Ankit is a python's trainer"

print(type(name))

name1='''Anikit is \none of a python's trainer
and also knows c++ too'''

print(name1)

name2='''Ankit is one of \n
python's trainer \n
and also knows c++'''
print(name2)

# converts str to int and int to strings
mobNum=123456789
print(type(mobNum))
print(mobNum)
mobNum=str(mobNum)
print(type(mobNum))
print(mobNum)
mobNum=int(mobNum)
print(type(mobNum))
print(mobNum)

# inbuild functions
name='zeeshan'
print(name.startswith('z'))
print(name.startswith('Z'))
print(name.endswith('n'))

name="My name is Zeeshan Ali"
print(name.count('a'))

fname="sachin"
print(fname.join("TEND"))

fname="Sachin"
lname="Tendulkar"
print(fname+" "+lname)

iname="Sachin"
print(iname.isdecimal())

jname='12345'
print(jname.isalpha())

name='pavan'
print(name.split('a'))

greetings='Good Morning'
print(greetings.index('r'))

sports="Basketball"
print(len(sports))
print(sports[7:9])
