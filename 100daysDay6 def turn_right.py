def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
move()
jump()
def jump2():
    turn_left()
    move()
    jump()

for step in range(0,6):
    jump2()







