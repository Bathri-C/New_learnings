import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S.States Game")
image="us-states-game-start//U_S_States.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("us-states-game-start//50_states.csv")
all_states=data.state.to_list()

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
guessed_state=[]
while len(guessed_state)<50:
    answer_state=screen.textinput(f"{len(guessed_state)}/50 Correct State","What's another state name?").title()  
    if answer_state=="Exit":
        missing_state=[state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        print(missing_state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn")
        break    
    if answer_state in all_states:
        guessed_state.append(answer_state)
        tommy=turtle.Turtle()
        tommy.hideturtle()
        tommy.penup()
        state_data=data[answer_state==data.state]
        tommy.goto(int(state_data.x),int(state_data.y))
        tommy.write(answer_state)

