#Write a program that switches the values stored in the variables a and b.

#Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.

a = 3
b = 5
print("the value of a is:",a)
print("the value of b is:",b)

temp = 0
temp = a
a = b
b = temp
print("the value of a is:",a)
print("the value of b is:",b)