import random
number=random.randint(1,100)
print("welcome to the number gussing game")
print("gusse the number between 1 to 100")
while True:
    guess=int(input("gusee the number"))
    if guess<number:
         print("too low try a bigger number")
    elif guess>number:
         print("too high try a smaller number")
    else:
         print("you guseee the correct number")
         break

         






