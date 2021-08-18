print("hello")
print("stmt-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
finally:
    print("the division is")
print("stmt-3")