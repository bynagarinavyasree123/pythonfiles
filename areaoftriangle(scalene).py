#write a python program to calculate the area of triangle
a=6
b=7
c=8
#caluclate the semiperimeter
s=(a+b+c)/2
#calculate the area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("the area of triangle ",area)
