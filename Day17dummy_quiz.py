from Day17quiz1 import Question
from Day17Question_data import question_data
from Day17question_brain import QuizBrain

question_bank =[]
for i in question_data:
    question_text =i["question"] 
    question_ans = i["correct_answer"]
    new_q = Question(question_text, question_ans) 
    question_bank.append(new_q)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()  
    

