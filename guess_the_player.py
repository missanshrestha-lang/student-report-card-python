import random
option=["messi","ronaldo","lewandoski","mbappe","salah"]
while True:
    player=random.choice(option)
    print("guess the player ")
    if player=="messi":  
        print("the player plays at rw")
        x=input("enter the player name ")
        if x!="messi":
            print("i will give you a hint")
            print("he is argentinian")
            x=input("enter the player name ")
            if x=="messi":
                print("congrats you guessed it right")
            else:
                 print("get some ball knowledge bro")   
        else:
             print("congrats you guessed it right")
             break

    elif player=="ronaldo":  
        print("the player plays at lw and the goat")
        x=input("enter the player name ")
        if x!="ronaldo":
            print("i will give you a hint")
            print("he is portuguese")
            x=input("enter the player name")
            if x=="ronaldo":
                print("congrats you guessed it right")
            else:
                print("get some ball knowledge bro")
            
        else:
            print("congrats you guessed it right")
            break

    elif player=="lewandoski":  
        print("the player plays at st")
        x=input("enter the player name ")
        if x!="lewandoski":
            print("i will give you a hint")
            print("he is polish")
            x=input("enter the player name ")
            if x=="lewandoski":
                print("congrats you guessed it right")
            else:
                print("get some ball knowledge bro")
            
        else:
            print("congrats you guessed it right")
            break

    elif player=="mbappe":  
        print("the player plays at st,currently knows as the best one")
        x=input("enter the player name ")
        if x!="mbappe":
            print("i will give you a hint")
            print("he is french")
            x=input("enter the player name ")
            if x=="mbappe":
                 print("congrats you guessed it right")
            else:
                print("get some ball knowledge bro")
            
        else:
            print("congrats you guessed it right")
            break

    elif player=="salah":  
        print("the player plays at rw")
        x=input("enter the player name ")
        if x!="salah":
            print("i will give you a hint")
            print("he is egyptian")
            x=input("enter the player name ")
            if x=="salah":
                print("congrats you guessed it right")
            else:
                print("get some ball knowledge bro")
            
        else:
            print("congrats you guessed it right")
            break

    



              
                
        