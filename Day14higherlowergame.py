import random
from Day14gamedata import data_game
#print(data_game)
from art14 import logo
print(logo)
score = 0
random_A = random.choice(data_game)
game=True
while game == True:
    print(f'compare A:{random_A["name"]},a {random_A["description"]}, from { random_A["country"]}')
    random_B = random.choice(data_game)
    if random_A ==  random_B:
        random_B = random.choice(data_game)
    print(f'compare B:{ random_B["name"]},a {random_B["description"]},from {random_B["country"]}')
    print(random_A["follower_count"])
    print(random_B["follower_count"])

    type_more = input("who has more followers Type 'A' or 'B':")
    if random_A["follower_count"] > random_B["follower_count"]:
        if type_more == "A":
            score +=1
            random_A =random_B
            random_B = random.choice(data_game)
            print(f"you win and your score is{score}")
        else:
            print("you loose")
            game =False

    elif random_A["follower_count"] < random_B["follower_count"]:
        if type_more =="B":
            score+=1
            random_A = random_B
            random_B = random.choice(data_game)
            print(f"you win and your score is{score}")
        else:
            print("you loose")
            game =False
            
print(f"your total score is{score}")


