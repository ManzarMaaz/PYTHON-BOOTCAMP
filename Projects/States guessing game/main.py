from turtle import Turtle, Screen
import pandas

writer = Turtle()

def show_state(input,x,y):
    writer.penup()
    writer.hideturtle()
    writer.goto(x,y)
    writer.write(input)
    

screen = Screen()
screen.title('U.S States Game')
screen.setup(725,491)
screen.bgpic('DAY 25/day-25-us-states-game-start/blank_states_img.gif')

data = pandas.read_csv('DAY 25/day-25-us-states-game-start/50_states.csv')

states_list = data['state'].to_list()

guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(title=f'Guess the State ({len(guessed_states)}/{len(states_list)})?',prompt="Write any State name ? or Exit to Quit").title()


    if user_input == 'Exit' :
        missing_states = []
        for states in states_list:
            if states not in guessed_states:
                missing_states.append(states)
        print(missing_states)
        pandas.DataFrame(missing_states).to_csv('Missing States.csv')
        break

    if (user_input in states_list) and (user_input not in guessed_states):
        state_data = data[data['state'] == user_input]
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()

        show_state(user_input,x_cor,y_cor)
        guessed_states.append(user_input)
