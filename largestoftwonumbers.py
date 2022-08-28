#largest of two numbers
a=float(input("enter the first value a:"))
b=float(input("enter the second valueb:"))
if(a>b):
    print("{0} is greater than {1}".format(a,b))
elif(b>a):
    print("{0} is greater than {1}".format(b,a))
else:
    print("both a,b are equal")
    
