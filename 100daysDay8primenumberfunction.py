#prime number
def prime_num(number):
    
    for i in range(2 ,number):
        print("i is",i)
        for j in range(i):
            print("j is",j)
            if j>1:
                if  i % j == 0:
                    #print(i,"it is not a prime number")
                    break
        else:
            print(i,"it is a prime number")
            
prime_num(number=5)