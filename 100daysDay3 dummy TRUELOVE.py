name_your = input("enter your name: ")
name_friend = input("enter another name: ")
lower_name = name_your.lower()
print(lower_name)
lower_friend = name_friend.lower()
print(lower_friend)
combined =lower_name + lower_friend
print(combined)
a = combined.count("t")
print("t presented no.of time",a)
b = combined.count("r")
print("r presented no.of time",b)
c = combined.count("u")
print("u presented no.of time",c)
d = combined.count("e")
print("e presented no.of time",d)
total_true = a+b+c+d
print(total_true)
x = combined.count("l")
print("l presented no.of times",x)
y = combined.count("o")
print("o presented no.of times",y)
z = combined.count("v")
print("v presented no.of times",z)
w = combined.count("e")
print("e presented no.of times",w)
total_love = x+y+z+w
print(total_love)
final= str(total_true)+str(total_love)
final1 = int(final)
print(final1)
if final1 < 10 or final1 > 90:
    print("your score is",final1,"you go together like coke and mentos")
elif final1 > 40 and final1 < 50:
    print("your score is",final1,"you are alright together ")
else:
    print("your score is",final1)

# input:ASdfszgfdtrueTre
#enter another name: Sffdflovuye
