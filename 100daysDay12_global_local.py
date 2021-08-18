#global and local variables friends = 1 is global variable  and friends = 2 is local variable
friends = 1
def family():
    def increase_friends():
        friends = 2
        print(f"friends inside function{friends}")
    increase_friends()
family()
print(f"friends outside function{friends}")



