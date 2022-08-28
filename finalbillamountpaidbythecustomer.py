#input net amount
amt=int(input("enter amount:"))
#caluclate amount with discount
if(amt>0):

    if amt<=5000:
        disc=amt*0.10
elif amt<=15000:
          disc=amt*0.15
elif amt<=25000:
         disc=0.20*amt
else:
        disc=0.5*amt
        print("discount amount:",disc)
        print("to be paid by costumer:",amt-disc)
        



