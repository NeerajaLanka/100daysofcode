# import random
# import string
# name_string = input("enter list of names seperated by comma.")
# name = name_string.split(",")
# print(name)
# a=random.choice(name)
# print(a)


import random
name_string = input("enter list of names seperated by comma.")
name = name_string.split(",")
print(name)
a = len(name)
print(a)
x = random.randint(0,a-1)
print(x)
y = name[x] 
print(y,"is going to pay the bill") 
