import math
def area_wall():
    height=int(input("enter height of wall is: "))
    width = int(input("enter width of wall is: "))
    coverage_percan = 5
    area= (height)*(width) 
    number_cans = area / coverage_percan
    total_cans = math.ceil(number_cans)
    print(f"no.of cans required { total_cans}")


    #print("no.of cans required:" ,round(number_cans))
area_wall( )