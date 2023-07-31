import turtle
import pandas

# Create the turtle
new_state = turtle.Turtle()
new_state.hideturtle()
new_state.penup()

# Create the screen
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Keep track of the score
score = 0
game_is_on = True
guessed_states = []

# Read the data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while game_is_on:
    user_input = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

    if user_input in all_states:
        score += 1
        state = data[data.state == user_input]
        x = int(state["x"].iloc[0])
        y = int(state["y"].iloc[0])
        new_state.goto(x, y)
        new_state.write(user_input)
        guessed_states.append(user_input)
    elif user_input == "Exit":
        not_guessed = [states for states in all_states if states not in guessed_states]
        new_data = pandas.DataFrame(not_guessed)
        new_data.to_csv("states_to_learn.csv")
        break
    elif score == 50:
        game_is_on = False

# Make a file with the States that weren't guessed
