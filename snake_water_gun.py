import random

user=int(input("Give a number (1,2,3) : "))  # 1-snake, 2-water, 3-gun
computer=random.randrange(1,4)

print("User input :",user)
print("Computer input :",computer)

if(user == computer): # draw case
    print("Draw !")

elif((user==1 and computer==2) or (user==2 and computer==3) or (user==3 and computer==1)): # win cases of user
    print("You Win!")

else:   # lose cases of user
    print("You Lose!")
