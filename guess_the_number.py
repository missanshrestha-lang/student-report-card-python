import random
number = random.randint(1,100)
while True:
    x= int(input("enter your guess"))
    if x<number:
        print("higher")
    elif x>number:
        print("lower")
    else:
        print("ur guess is correct")