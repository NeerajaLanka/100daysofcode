def prime_num():
    number= int(input("enter a number to  find prime or not: "))
    for i in range(2,number):
        
        if number % i ==0:
            print("it is not a prime num ",number)
            break
            
    else:
        print("it is prime")
prime_num()