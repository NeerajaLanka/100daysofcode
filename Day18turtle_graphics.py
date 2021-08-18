from turtle import Turtle, Screen
turtle_obj_1 = Turtle()
turtle_obj_1.shape("turtle")
# #draw a square
# for i in range(1,5):
#     turtle_obj_1.forward(100)
#     turtle_obj_1.right(90)

# #draw a dashed line
# for _ in range(5):
#     turtle_obj_1.forward(10)
#     turtle_obj_1.penup()
#     turtle_obj_1.forward(10)
#     turtle_obj_1.pendown()

#draw a triangle,square
for _ in range(1,4):
    turtle_obj_1.color("green")
    turtle_obj_1.forward(100)
    turtle_obj_1.right(120)
for i in range(1,5):
    turtle_obj_1.color("red")
    turtle_obj_1.forward(100)
    turtle_obj_1.right(90)
for _ in  range(1,6):
    turtle_obj_1.color("light blue")
    turtle_obj_1.forward(100)
    turtle_obj_1.right(72)
for _ in range(1,7):
    turtle_obj_1.color("light green")
    turtle_obj_1.forward(100)
    turtle_obj_1.right(60)
for _ in range(1,8):
    turtle_obj_1.color("blue")
    turtle_obj_1.forward(100)
    turtle_obj_1.right(51.1) 
for _ in range(1,9) :
    turtle_obj_1.color("orange")
    turtle_obj_1.forward(100)
    turtle_obj_1.right(45) 
for _ in range(1,10):
    turtle_obj_1.color("indigo")
    turtle_obj_1.forward(100)
    turtle_obj_1.right(40)
for _ in range(1,11):
    turtle_obj_1.color("pink")
    turtle_obj_1.forward(100)
    turtle_obj_1.right(36)        
screen = Screen()
screen.exitonclick()