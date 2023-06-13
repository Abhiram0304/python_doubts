import random

hcount=0
toss=0
while(hcount<3):
    flip=random.randrange(0,2)
    #flip=0 --- head
    #flip=1 --- tail
    if(flip==0):
        hcount+=1
        toss+=1
        print("H",end=" ")
    else:
        hcount=0
        toss+=1
        print("T",end=" ")
print()
print("No of tosses :",toss)