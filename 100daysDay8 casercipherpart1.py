alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(shift_text,shift_amount):
    a =" "
    for i in text:
        x = alphabet.index(i)
        y = x+shift
        z = alphabet[y]
        a = a + z        
    print("encodede text is:",a)
#encrypt(shift_text=text,shift_amount=shift)
def decrypt(decode_text,decodeshift_amount):
    a =" "
    for i in text:
        x = alphabet.index(i)
        y = x-shift
        z = alphabet[y]
        a = a + z        
    print("decoded text is:",a)
#decrypt(decode_text=text,decodeshift_amount=shift)
if direction == "encode":
    encrypt(shift_text=text,shift_amount=shift)
if  direction =="decode":
    decrypt(decode_text=text,decodeshift_amount=shift)