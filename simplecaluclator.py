#python program to make a simple caluclator
print("please select the operation you want to perform 1.addition 2.subtraction 3.multiplication 4.divison")
opt=int(input("choose operation from 1,2,3,4"))
n1=int(input("first number"))
n2=int(input("second number"))
if opt==1:
    print(n1, '+', n2, '=', n1+n2)
elif opt==2:
    print(n1, '-', n2, '=', n1-n2)
elif opt==3:
    print(n1, '*', n2, '=', n1*n2)
elif opt==4:
    print(n1, '/', n2, '=', n1/n2)
else:
    print("invalid number")
    
