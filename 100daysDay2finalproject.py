print("welcome to the tip calculator")
food_bill = input("what was total bill? ")
tip_percent = input("how much tip percent to pay: ")
tip = round((food_bill/tip_percent),2)
print("tip",tip)
final_bill = food_bill + tip
print("bill",final_bill)
number_persons = input("no.of persons? ")
each_person = round((final_bill /number_persons),2)
print(each_person)