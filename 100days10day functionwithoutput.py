#firstname capital
def format_name():
    f_name = "apPLe"
    l_name = "boAt"
    print(f_name.capitalize()+ " " + l_name.capitalize()  )
format_name()


#firstname capitalize with title method
def format_Name(f_name,l_name):
    """it formates first name and lasrt name by using title
    keyword"""
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name}  {last_name}"
name = format_Name("APPLE","ApplE")
print(name)    