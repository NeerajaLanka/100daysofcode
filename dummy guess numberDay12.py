import random

#from lognumber import logo_1 
#print(logo_1 )
print(" welcome to  guess the number")
random_number = random.randint(1,100)
print(random_number)
#guess_num = int(input("make a guess"))
def level():
    if choose_type== "easy":
        print("you have 10 attempts")
        attempts = 10
        return  attempts
    elif choose_type== "hard":
        print("you have 5 attempts")
        attempts =5 
        return  attempts


def compare():
    if guess_num < random_number:
        print("Too low")
        
    elif guess_num > random_number:
        print("Too high")
    else:
        print("guess is correct")
choose_type = input("choose a difficulty as hard or easy")
attempt = level()
guess_num = 0
while guess_num != random_number:
    guess_num = int(input("make a guess"))
    print(f"you have {attempt} many attempts remaining")
    compare()
    attempt -=1
    if  attempt == 0:
        print("you loose")
        break
    elif guess_num == random_number :
        attempt+=1
        print(f"you won the game in {attempt} attempts")
        
    else:
        print(f"guess again you have {attempt}remaning")




    
    
