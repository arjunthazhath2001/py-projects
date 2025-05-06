import html

class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list= question_list
        self.score=0
    
    def next_question(self):
        current_question= self.question_list[self.question_number]
        self.question_number+=1
        question=html.unescape(current_question.text)
        return f"Q.{self.question_number} {question} (True/False)?: "
        # ans= input(f"Q.{self.question_number} {question} (True/False)?: ")   
        # self.check_answer(ans,current_question.answer)
    
    def still_has_questions(self):
        return self.question_number<len(self.question_list)
    
    def check_answer(self,ans,current_ans):
        if ans.lower()==current_ans.lower():
            self.score+=1
            return True
        else:
            return False
 
            
        
        