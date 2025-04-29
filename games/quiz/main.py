from data import question_data
from quiz_brain import QuizBrain
from quiz_model import Question

question_bank=[]

for q in question_data:
    question_bank.append(Question(q["question"],q["correct_answer"]))



q= QuizBrain(question_bank)

while q.still_has_questions():
    q.next_question()