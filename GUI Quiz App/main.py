import html
import requests
from question import Question
from quiz_brain import QuizBrain
from user_interface import UserInterface

parameters = {
    "amount": 10,
    "type": "boolean"
}

end_point = "https://opentdb.com/api.php"
response = requests.get(url=end_point, params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
questions_list: [Question] = []

for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    questions_list.append(Question(text=question_text, answer=question_answer))

quiz_brain = QuizBrain(questions_list=questions_list)
user_interface = UserInterface(quiz_brain=quiz_brain)