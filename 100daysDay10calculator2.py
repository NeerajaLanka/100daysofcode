#calculator
#from art import logo
#addition
import math
def squreroot(n1):
    return math.sqrt(n1)
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
operations={"+":add,"-":sub,"*":mul,"/":div, "^":squreroot }
def calculator():
    #print(logo)
    first_num= float(input ("enter first number: "))
    for operator in operations:
        print(operator)
    continue_1 = True  
    while continue_1 == True:
        
        choice = input ("which one do you want to performn?")
        if choice == "^":
            function = operations[choice]
            answer = function(n1=first_num)
            print(f"{first_num} squreroot is {answer}")

        else:
            second_num = float(input("enter another number"))
            function =operations[choice]
            answer = function(n1=first_num,n2=second_num)
            print(f"{first_num} {choice} {second_num} = {answer}")
        answer_input = input("do you want to continue  with above answer yes or no")
    
        if answer_input == "yes":
            first_num = answer
        
        else:
            continue_1 = False
            sart_continue = input("do you want to start calculating from begining?yes or no")
            if sart_continue == "yes":
                calculator()
            else:
                print("thank you")
calculator()       





