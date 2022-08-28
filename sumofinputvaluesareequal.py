#write a python program to caluclate the sum of numbers if input numbers are different and also find price of sum if input values are equal
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
sum=a+b+c
if(a==b==c):
    sum=sum*3
    print("the sum is",sum)
else:
    print("the sum is",sum)
