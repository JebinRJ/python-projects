import random
def check():
    mind=random.randint(1,11)
    guess=int(input("Enter your guess : "))
    
    if guess==mind:
        print("Your guess is right")
    elif guess>mind:
        print("Your guess is high")
        check()
    else:
        print("Your guess is low")
        
        check()
check()
