from re import X


addTwoNumbers=lambda x,y: x+y
print(addTwoNumbers(2,3))
print(addTwoNumbers)

areaOfCube=lambda l,b,*h: l*b*h
print(areaOfCube(3,3,3))
print(areaOfCube(5,6,7))

print("Area of Shape")
areaOfShape=lambda l,b,h,**z: l*b*h*list(z.values())
print(areaOfShape(3,4,4,X=3,Y=4))
areaOfShape=lambda l,b,h,**z: l*b*h*list(z.keys())
print(areaOfShape(3,4,4,X=3,Y=4))

print("Example for f'string")
sport=input("Please type your sport : ")
score=input("Please type your score : ")
print(f"I like to play {sport} and i scored {score}")

rice=8.37865
milk=6.986754

print(f"The cost of rice is {rice:.2f} and the cost of milk is {milk:.3f}")
