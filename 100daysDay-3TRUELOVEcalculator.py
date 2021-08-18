your_name = input("enter your name: ")
friend_name = input("enter another name: ")
your_name1 = your_name.lower()
print(your_name1)
y=list(your_name1)
print(y)
x =["t","r","u","e"]
sum=0
for i in range(0,len(x)):
    while x[i] in y:
        z= y.count(x[i])
        print("the letter",x[i],"is present",z,"times")
        sum+=z
        i+=1
print("yes it is present",sum)


# print(your_name1.count())
# friend_name1 = friend_name.lower()
# print(friend_name1)