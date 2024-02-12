from question_model import Question
from data import question_data
from quiz_brain import Quizzbrain
question_bank=[]
for line in question_data:
    question=line["text"]
    answer=line["answer"]
    question_bank.append(Question(question,answer))

quiz=Quizzbrain(question_bank)
quiz.questionnaire()
