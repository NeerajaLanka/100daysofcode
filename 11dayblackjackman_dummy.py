import random
print("welcome to balack jack")
list_1 = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_choice =[ ]
sum= 0
for i in range(0,2):
    user_choice_variable = random.choice(list_1)
    user_choice.append(user_choice_variable) 
    sum+=user_choice[i]
print(f"user selection{user_choice} and current score {sum}")
computer_choice =[ ]
computer_choice_variable = random.choice(list_1)
computer_choice.append(computer_choice_variable)
computer_sum = 0 
computer_sum+= computer_choice_variable
print(f"computer sum is {computer_sum}")
print(f"computer choice is {computer_choice}")
if sum == 21 and computer_choice[0] < 21:
    print("user wins" )
else:
    continue_1 = True
    while continue_1 ==True:    
        repeat = input("do you want to take yes or no? ")
        if repeat == "yes":
            user_choice_variable = random.choice(list_1)
            if  sum > 10 and user_choice_variable == 11:
                user_choice_variable = 1
                user_choice.append(user_choice_variable)
                sum+=user_choice_variable
                print(f"user selection with repeat {user_choice} and sum is  {sum}")

            else:
                user_choice.append(user_choice_variable)
                sum+= user_choice_variable
                print(f"user selection with repeat {user_choice} and sum is  {sum}")
            if sum >= 21:
                continue_1 = False
                print("test--------1")
        else:
            continue_1 = False
computer_choice_variable = random.choice(list_1)
computer_choice.append(computer_choice_variable) 
computer_sum+= computer_choice_variable
if computer_sum <=21 and sum <=21: 
    if  computer_sum == sum :
            print(f"computerscore is {computer_sum}and user sum is {sum} it is draw") 
    elif computer_sum < sum:
        print(f" computerscore is {computer_sum}and user sum is {sum} so user wins")
    else:
        print(f"computerscore is {computer_sum}and user sum is {sum} so computer wins")
elif computer_sum >21 and sum <=21  :
    print(f"computerscore is {computer_sum}and user sum is {sum} so user wins ,computer burst")
elif computer_sum <=21 and sum >21  :
    print(f"computerscore is {computer_sum}and user sum is {sum} so user burst ,computer wins")
else:
    print(f"computerscore is {computer_sum}and user sum is {sum} so it got burst")


