from Day17quiz1 import Question
from Day17Question_data import question_data
from Day17question_brain import QuizBrain
question_bank =[]
for i in question_data:
    question_text =i["text"] 
    question_ans = i["answer"]
    new_q = Question( question_text, question_ans) 
    question_bank.append(new_q)
quiz = QuizBrain(question_bank)
quiz.next_question()  


