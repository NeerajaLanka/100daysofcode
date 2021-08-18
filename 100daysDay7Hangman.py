import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

len_stages = len(stages)
print(len_stages )
lives = 6
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
k = 0
while k < (length_chosen):
    guess = input("enter a letter: ").lower()
    for j in range(length_chosen):
        if chosen_word[j] == guess :
            display[j] = guess
            
            print(display)
     
    k+=1      
           
    
    if  guess not in chosen_word :
        lives -= 1
       
        if lives ==0:
            print("you loose the game")
    if "_" not in display:
        print("you won")        
    print(stages[lives])
       

           

