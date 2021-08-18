alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def ceaser(input_text,input_shift):
    result_str = " "
    if direction =="encode":
        for letter in text:
            a = alphabet.index(letter)
            b = a+ shift
           # c = alphabet[b]
            result_str+= alphabet[b]
        print("encoded text is: ",result_str)
    elif direction == "decode":
        for letter in text:
            a = alphabet.index(letter)
            b = a - shift
           # c = alphabet[b]
            result_str+= alphabet[b]
        print("decoded text is: ",result_str)
ceaser(input_text=text,input_shift=shift)

        