from data import question_data
from quiz_brain import QuizBrain
from quiz_model import Question
from ui import QuizInterface

question_bank=[]

for q in question_data:
    question_bank.append(Question(q["question"],q["correct_answer"]))



q= QuizBrain(question_bank)
q_ui= QuizInterface(q)

# while q.still_has_questions():
#     q.next_question()