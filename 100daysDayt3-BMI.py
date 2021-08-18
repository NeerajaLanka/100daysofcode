# #Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# #It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
# https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

# Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

weight_person = input("please enter your weight in kg: ")      #weight in kg 55
height_person = input("please enter your height in meters: ")  #height 5 feet 4 inches in meters is 1.63
BMI = weight_person/(height_person**2)
print(BMI)
if BMI < 18.5:
    print("you are under weight")
elif BMI < 25:
    print("you have normal weight")
elif BMI < 30:
    print("you are slightly over weighted")
elif BMI< 35:
    print("you are obesse")
else:
    print("you are clinically obbese")