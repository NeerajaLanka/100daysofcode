import random
list1 = ["apple","banana","kiwi","pineapple","papayas"]
chosenword = random.choice(list1)
print(chosenword)
wordlength = len(chosenword)
print(wordlength)
display = []
for i in range(wordlength):
    display += " "
while wordlength >= (len(display)):
    guess = input("Guess a letter: ").lower()  
    if guess in display:
        print(guess)
    for j in range(wordlength):
        letter = chosenword[j]
        if letter == guess:
            display[j] = letter
        
            print("right")
        else:
            print("wrong")
    print("out of range")