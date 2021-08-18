#rock paper scissors game against computer.
#rock wins against scissors
#scissors wins against paper
#paper wins against rock.
import random

rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images =[rock,paper,scissors]
user_choose = int(input ("What do you choose type 0 for rock, 1 for paper,2 for scissors  "))
print(game_images[user_choose])
computer_choose = random.randint(0,2)
print(game_images[computer_choose])

if user_choose == 0 and computer_choose == 2:
    print("you won")
elif user_choose == 2 and computer_choose == 1:
    print("you won")
elif user_choose == 1 and  computer_choose == 0:
    print("you won")
elif user_choose == computer_choose:
    print("it's draw")
else:
    print("you loose")

