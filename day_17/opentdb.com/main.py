from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for items in question_data:
        new_q = Question(items["question"], items["correct_answer"])
        question_bank.append(new_q)

quiz = QuizBrain(question_bank)
is_true = True


while is_true:
        try:
                quiz.next_question()

        except:
                print("You finish the quiz!")
                break





#print(question_bank[0].text)
