import random
class Quizzbrain:
    def __init__(self, question_list):
        self.question_number=1
        self.question_list=question_list
        self.score=0

    # def next_question(self):
    #     current_question=self.question_list[self.question_number]
    #     self.question_number+=1
    #     print(f"Q.{self.question_number}: {current_question.text} (True/False)")
    # def still_has_question(self):
    #     if self.question_number<len(self.question_list[self.question_number].text):
    #        return True
    #
    def questionnaire(self):
        #display the question
        score=0
        for question in self.question_list:
            print(f"Question{self.question_number}: {question.text}")
            self.question_number+=1
            # get the user's answer
            ans=input().lower()
            if question.answer.lower()==ans:
                score+=1
        print(f"Your score is {score}")



