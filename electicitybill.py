units=int(input("please enter the number of units you consumed in a month"))
if(units<=100):
    payamount=units*1.5
    fixedcharge=25.00
elif(units<=200):
    payamount=(100*1.5)+(units-100)*2.5
    fixedcharge=50.00
elif(units<=300):
    payamount=(100*1.5)+(200-100)*2.5+(units-200)*4
    fixedcharge=75.00
elif(units<=350):
    payamount=(100*1.5)+(200-100)*2.5+(300-200)*4+(units-300)*5
    fixedcharge=100.00
else:
    payamount=0
    fixedcharge=1500.00
    total=payamount+fixedcharge
    print("\nelectricitybill=%f"%total)
    print("the value of total is",total)




    
