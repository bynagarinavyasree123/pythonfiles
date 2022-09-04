#logical operator
a=int(input("enter the values of a"))
b=int(input("enter the values of b"))
c=((a>b)&(b>20))
print("the value of c is %d",c)
d=((a<b)|(a>10))
print("the value of d is %d",d)
e=not (a>b)
print("the value of e is %d",e)
