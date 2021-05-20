class Score:
    def __init__(self, total_of_states):
        self.current_score = 0
        self.total_of_states = total_of_states

    def add_point(self):
        self.current_score += 1