import turtle
import pandas

# create screen from the US States gif image
turtle.screen = turtle.Screen()
turtle.screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.screen.addshape(image)
turtle.shape(image)

turtle_state = turtle.Turtle()
turtle_state.hideturtle()


# read the csv file
data = pandas.read_csv("50_states.csv")

# create a list of the states column
all_states = data.state.to_list()

# keep track of the guesses
guessed_states = []
missed_states = []
game_on = 0

# create .csv with list of states that the user missed.
def result_sheet():
    for state in all_states:
        if state not in data.state:
            missed_states.append(state)
            df = pandas.DataFrame(missed_states)
            df.to_csv("Missed_States.csv")
    print(missed_states)

while len(guessed_states) < 50:
# popup window for input
    answer_state = turtle.screen.textinput(title=f"{game_on}/50 Guess the State",
                                    prompt="What's another state's name? ").title()
    if answer_state == "Exit" or answer_state == "exit":
        result_sheet()
        turtle.screen.bye()
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        game_on += 1

    if answer_state not in all_states:
        answer_state
        game_on += 1


turtle.screen.exitonclick()