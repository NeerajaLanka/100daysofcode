'''
Author: Neeraja Lanka
Description: This Proram calculate pizza cost with a sales tax
'''
number_of_pizzas=eval(input("how many pizzas do you want: "))
pizza_cost=eval(input("how much does each pizza cost: "))
subtotal=number_of_pizzas*pizza_cost
tax_rate=0.08
sales_tax=subtotal*tax_rate
total=subtotal+sales_tax
print("the total cost is",total)
print("This include $ ",subtotal,"for the pizza and: ")
print("$",sales_tax,"in sales tax: ")
