from turtle import Turtle,Screen
tig = Turtle()
screen_saver = Screen()
def my_function1():
    tig.forward(30)
def my_function2():
    tig.backward(30)
def my_function3():
    new_heading  = tig.heading()+10
    tig.setheading(new_heading) 
def my_function4():
    new_heading  = tig.heading()-10
    tig.setheading(new_heading) 
def my_function5():
    tig.clear()     
screen_saver.listen()
screen_saver.onkey(key ="W",fun = my_function1)
screen_saver.onkey(key ="S",fun = my_function2)
screen_saver.onkey(key ="A",fun = my_function3)
screen_saver.onkey(key ="D",fun = my_function4)
screen_saver.onkey(key ="C",fun = my_function5)

screen_saver.exitonclick()