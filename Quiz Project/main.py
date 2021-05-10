# Andrés López Esquivel
# 05/09/2021
# Project: Quiz Brain

from data import question_data
from question import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_questions():
    quizBrain.next_question()

print("You've completed the quiz.")
print(f"Your final score:{quizBrain.user_score}/{len(quizBrain.question_list)}")