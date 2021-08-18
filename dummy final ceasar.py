alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(input_text,input_shift,direction1):
    result_text = ""
    if (direction1 =="encode"):
        for i in input_text:
            if i not in alphabet:
                result_text += i
            else: 
                v= alphabet.index(i)
                w=(v+input_shift)%26
                result_text += alphabet[w]
        print(result_text)

        
    elif(direction1 == "decode"):
        for i in input_text:
            if i not in alphabet:
                result_text +=i
            else:    
                v= alphabet.index(i)
                w=(v-input_shift)%26
                result_text +=alphabet[w]
        print(result_text)

from art import logo
print(logo)
execute=input("do you want to encode or decode any string? yes or no")

while execute == "yes":
    direction = input("type encode for encryption and decode for decrption:")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(input_text=text,input_shift=shift,direction1=direction)
    repeat =input("do you want to repeate the coding? yes or no")
    if repeat == "no":
        execute = "no"
print("good bye") 