# Based on the "Can you name the US states?" game from sporcle.com
# Game link: https://www.sporcle.com/games/g/states

from turtle import Screen
from dataManager import DataManager
from writer import Writer
from score import Score

US_MAP_PATH = "./blank_states_img.gif"

data_manager = DataManager()
screen = Screen()

screen.title("Can you name the US states?")
screen.bgpic(US_MAP_PATH)

writer = Writer()
score = Score(data_manager.number_of_states)

while score.current_score != score.total_of_states:

    title = f"{score.current_score}/{score.total_of_states} states guessed"
    state_name_entered = screen.textinput(title=title, prompt="Enter another US state's name").title()

    if state_name_entered.lower() == "exit":
        data_manager.save_states_to_learn()
        break

    if data_manager.state_exists(state_name_entered):
        state_position = data_manager.state_data(state_name_entered)
        writer.write_state_name(state_name_entered, state_position)
        data_manager.remove_state(state_name_entered)
        score.add_point()

screen.exitonclick()
