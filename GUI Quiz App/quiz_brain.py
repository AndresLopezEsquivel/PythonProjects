from question import Question


class QuizBrain:

    def __init__(self, questions_list: [Question]):
        self.question_number = 0
        self.question_list = questions_list
        self.current_question_text: str = ""
        self.current_question_answer: str = ""
        self.user_score = 0
        self.user_score_text = f"Score: 0/{len(self.question_list)}"

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question_text = self.question_list[self.question_number].text
        self.current_question_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        return f"Q{self.question_number}. {self.current_question_text}: (True/False)."

    def check_answer(self, user_answer: str):
        if user_answer.lower() == self.current_question_answer.lower():
            self.user_score += 1
            self.user_score_text = f"Score: {self.user_score}/{len(self.question_list)}"
