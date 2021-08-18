pizza_size = str(input("which size of pizza do you want? : "))
print(pizza_size)
ppizza =str(input("do you want ppizza?  y or n :"))


if pizza_size == "small":
    s_bill = 15
    print(s_bill)
    if ppizza == "y":
        s_bill +=2
    print("your pizza bill is : ",s_bill)
elif pizza_size == "medium":
    m_bill = 20
    print(m_bill)
    if ppizza == "y":
        m_bill +=3
    print("your pizza bill  is : ",m_bill)
else:
    l_bill = 25
    print(l_bill)
    if ppizza == "y":
        l_bill +=3
    print("your pizza bill is : ",l_bill)

