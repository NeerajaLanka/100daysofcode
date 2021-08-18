class QuizBrain:
    def __init__(self,q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0
        
        
    def next_question(self):
        current_question =  self.q_list[self.q_num]
        self.q_num +=1
        ans=input(f"Q.{self.q_num}:{current_question.text}: (True/False) : ")
        self.check_answer(ans,current_question)
    
    def still_has_question(self):
        return self.q_num <= len(self. q_list)
    
    def check_answer(self,ans,current_question):
        if (current_question.answer) == ans:
            print("you got right answer")
            self.score +=1
            print(f"your total score is {self.score}/{self.q_num}")
        else:
            print("you are wrong")
            print(f"correct answer is {current_question.answer}")
            print(f"your total score is {self.score}/{self.q_num}")


