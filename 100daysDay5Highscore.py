score = [78,65,89,86,55,91,64,89]
#print(max(score))
list_1 = []
a=0
for i in score:
    if a < i:
        a = i
print(a)



#1 to 100 sum
sum = 0
for i in range(1,101):
    sum +=i
print(sum)
