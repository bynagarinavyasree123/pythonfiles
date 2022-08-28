print("entered the marks obtained in five subjects")
markone=int(input())
marktwo=int(input())
markthree=int(input())
markfour=int(input())
markfive=int(input())
tot=markone+marktwo+markthree+markfour+markfive
avg=tot/5
print("the avg of 5 subjects is",avg)
if avg>=91 and avg<=100:
    print("your grade is A1")
elif avg>=81 and avg<=91:
    print("your grade is A2")
elif avg>=71 and avg<=81:
    print("your grade is B1")
elif avg>=61 and avg<=71:
    print("your grade is B2")
elif avg>=51 and avg<=61:
    print("your grade is C1")
elif avg>=41 and avg<=51:
    print("your grade is C2")
elif avg>=31 and avg<=41:
    print("your grade is D")
elif avg>=21 and avg<=31:
    print("your grade is E1")
elif avg>=0 and avg<=21:
    print("your grade is E2")
else:
    print("invalid input")
