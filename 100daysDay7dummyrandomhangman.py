#program to generate random word and guess that word.
import random
list_1 =["apple","banana","grapes","cherry","mango","kiwi"]
chosen_word = random.choice(list_1)
print(chosen_word)
length_chosen = len(chosen_word)
print(length_chosen)
list_chosen = list(chosen_word )
display=[ ]
for i in range(length_chosen):
    display+= "_"
print(display)
k=0
while k < (length_chosen):
    guess = input("enter a letter: ").lower()
    for j in range(length_chosen):
        if chosen_word[j] == guess:
            display[j] = guess
    print(display)
    k+=1
if "_" in display:
    print("you loose")  
else:
    print("you win")  