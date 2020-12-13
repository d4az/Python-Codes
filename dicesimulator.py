import random

i =0

while( i < 100):
     x = str(input("Enter Y To Roll The Dice Again : "))
     if(x == 'y'):
        num= random.randint(1, 6)

        if(num ==1):
            print("(-----------)")
            print("(           )")
            print("(     0     )")
            print("(           )")
            print("(-----------)")
        elif(num==2):
            print("(-----------)")
            print("(           )")
            print("(   0   0   )")
            print("(           )")
            print("(-----------)")
        elif(num==3):
            print("(-----------)")
            print("(           )")
            print("(   0 0 0   )")
            print("(           )")
            print("(-----------)")
        elif(num==4):
            print("(-----------)")
            print("(    0 0    )")
            print("(    0 0    )")
            print("(           )")
            print("(-----------)")
        elif(num==5):
            print("(-----------)")
            print("(    0 0    )")
            print("(    0 0    )")
            print("(     0     )")
            print("(-----------)")
        else:
            print("(-----------)")
            print("(    0 0    )")
            print("(    0 0    )")
            print("(    0 0    )")
            print("(-----------)")
        
     else:
         break
