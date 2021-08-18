#password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password =[letters,numbers,symbols]
print(password)

a =random.randint(password)
print(a)

# for i in range(nr_letters):
#     a = random.randint(i)
#     print(letters[a])
# b = random.choice(nr_numbers)
# c = random.choice(nr_symbols,symbols)

# print(b)
# pringt(c)
# total_random = a+b+c
# print("total random numbers: ",list(total_random))

# for a in range(0,nr_letters+1):
#     for b in range(0,nr_numbers+1):
#         for c in range(0,nr_symbols+1):
#             print(a)
#             print(b)
#             print(c)
#         print(a+b+c)
# # for i in range(0,total_random):
# #     print()
