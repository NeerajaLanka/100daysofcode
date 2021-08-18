import random
#from lognumber import logo_1 
#print(logo_1 )
print(" welcome to  guess the number")
random_number = random.randint(1,100)
print(random_number)
#guess_num = int(input("make a guess"))

def compare():
    if guess_num < random_number:
        print("Too low")
    elif guess_num > random_number:
        print("Too high")
    else:
        print("guess is correct")
choose_type = input("choose a difficulty as hard or easy")
if choose_type== "easy":
    print("you have 10 attempts")
    attempts = 10
    guess_num = 0
while guess_num != random_number:
    guess_num = int(input("make a guess"))
    print(f"you have {attempts} many attempts remaining")
    compare()
    attempts -=1
    if  attempts == 0:
        print("you loose")
        break
    else:
        print(f"guess again you have {attempts}remaning")



    
    
# elif choose_type== "hard":
#     print("you have 5 attempts")
#     attempts = 5
# else:


