# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

# https://www.youtube.com/watch?v=xX96xng7sAE

# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

# e.g. The year 2000:
#to check leap year range
def leapyear():
    for i in range(1900,2000):
        if i%400 ==0:
            print(i,"is leap year")
            
        elif  i%4 ==0:
            print(i,"is leap year")
        else:
            print(i,"not leap year" )    
leapyear()