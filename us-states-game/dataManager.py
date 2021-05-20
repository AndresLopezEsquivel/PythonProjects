import pandas as p

US_STATES_CSV_PATH = "50_states.csv"
STATE_NAME_COLUMN = "state"
STATES_TO_LEARN_FILE_PATH = "states_to_learn.csv"

class DataManager:

    def __init__(self):
        self.us_states_data = p.read_csv(US_STATES_CSV_PATH)
        self.list_name_of_states = self.us_states_data[STATE_NAME_COLUMN].to_list()
        self.number_of_states = len(self.us_states_data)
        print(self.list_name_of_states)

    def state_data(self, state_name):
        state_data_result = self.us_states_data[self.us_states_data[STATE_NAME_COLUMN] == state_name]
        state_data_index = state_data_result.index[0]
        x_position = state_data_result["x"][state_data_index]
        y_position = state_data_result["y"][state_data_index]
        return x_position, y_position

    def state_exists(self, state_name):
        return True if state_name in self.list_name_of_states else False

    def remove_state(self, state_name):
        self.list_name_of_states.remove(state_name)

    def save_states_to_learn(self):
        states_to_learn = p.DataFrame(self.list_name_of_states)
        states_to_learn.columns = ["state"]
        states_to_learn.to_csv(STATES_TO_LEARN_FILE_PATH)
