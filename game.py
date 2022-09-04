#python program to design guess the number game
#import random
#mynum=random.randint(0,9)
mynum=8
print("i have a number in my mind(0-9).can u guess it?")
while True:
    usernum=int(input("enter your guess:"))
    if (mynum==usernum):
        print("yes you are right")
        break
    elif(mynum>usernum):
        print("my number is greater than user number")
    else:
        print("my number is lesser than user number")
