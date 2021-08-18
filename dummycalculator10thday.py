#calculator
#addition
def add(n1,n2):
    return n1+n2
# #subtraction
def sub(n1,n2):
    return n1-n2
# #multiplication
def mul(n1,n2):
    return n1*n2
#  division
def div(n1,n2):
    return n1/n2
continue_1 = "yes"
first_num= int(input ("enter first number: "))
while continue_1 == "yes":
    operations={"+":add,"-":sub,"*":mul,"/":div }
    for operator in operations:
        print(operator)
    choice = input ("which one do you want to performn?")
    second_num = int(input("enter another number"))
    function = operations[choice]
    answer = function(n1=first_num,n2=second_num)
    print(f"{first_num} {choice} {second_num} = {answer}")
    second_choice = input("do you want to continue  with above answer yes or no")
    if second_choice == "yes":
        for operator in operations:
            print(operator)
        second_selection = input("which one do you want to perform?")
        num3 = int(input("enter another number to do: "))
        function = operations[second_selection]
        answer1 = function(answer,num3)
        print(f"{answer} {second_selection} {num3} = {answer1 }")
    else:
        continue_1="no"
        