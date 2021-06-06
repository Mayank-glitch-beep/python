import random
while(True):
    secnum=random.randint(1,10)
    guessnum=int(input("enter the number"))
    if(not guessnum):
        print("Invalid input")
        break
    else:
        if(guessnum==secnum):
            print("player wins and computer loses")
        else:
            print("player loses and computer wins")


        
        
            


        
