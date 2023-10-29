import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S states Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pd.read_csv("50_states.csv")
all_states = state_data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # missed_states = []

        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)

        # getting missed state using list comprehension
        missed_states = [state for state in all_states if state not in guessed_states]

        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        selected_state = state_data[state_data["state"] == answer_state]
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(int(selected_state["x"].iloc[0]), int(selected_state["y"].iloc[0]))
        state_turtle.write(answer_state)

screen.exitonclick()

