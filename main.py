from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    combination_of_text_answer = Question(question_text , question_answer)
    question_bank.append(combination_of_text_answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")