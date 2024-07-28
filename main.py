import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("USA States Identification")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(800, 600)
turtle.shape(image)

score = 0

data = pandas.read_csv("50_states.csv.csv")
guessed = []

for i in range(0, 50):
    list_state = data["state"]
    l = list_state.to_list()
    print(l)
    time.sleep(0.1)
    answer = screen.textinput(f"Guess The State {score}/50", "Whats another state name?").title()
    if answer in l:
        if answer not in guessed:
            score += 1
            l = data[data["state"] == answer]
            x_cor = int(l["x"])
            y_cor = int(l["y"])
            print(x_cor, y_cor)
            tim = turtle.Turtle()
            tim.hideturtle()
            tim.penup()
            tim.goto(x_cor, y_cor)
            tim.write(f"{answer}")
            guessed.append(answer)

result = turtle.Turtle()
result.hideturtle()
result.penup()
result.goto(0, 0)

if score == 50:
    result.write("You won!", align="center", font=("Courier", 20, "normal"))
else:
    result.write(f"No More Chances Left. You Lost! Score: {score}", align="center", font=("Courier", 20, "normal"))
turtle.done()
screen.exitonclick()






