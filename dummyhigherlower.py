import random
from Day14gamedata import data_game
import art

def getdata():

    return random.choice(data_game)

def compare(sc):
    if a["follower_count"] >  b["follower_count"]:
        if guess=="a":
           sc+=1
           #print(f"you won and score is {sc}")
           return sc
    elif a["follower_count"] <  b["follower_count"]:
        if guess=="b":
            sc+=1
            #print(f"you won and score is {sc}")
            return sc
    else:
        game=False

    a=getdata()
    b =getdata()
ans = compare(sc)
print(f"{sc}")

sc =0
game=True
while game is True:
    from art import logo
    #print(logo)
    print(f'compare A : {a["name"]},{a["description"]},{a["country"]}')
    from art import vs
    #print(vs)
    b=getdata()
    print(f'compare B : {b["name"]},{b["description"]},{b["country"]}')
    print(a["follower_count"])
    print(b["follower_count"])
    guess=input("who has many followers? a OR b : ")
    
    compare(score)
    sc=compare(score)
    print(f"you won and score is {sc}")
    

    if score <= sc:
        print("score is ", score)
        print("sc is ",sc)
        a=b
    else:
        game=False
     