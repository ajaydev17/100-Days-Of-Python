class QuizBrain:

    # definition of the constructor
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        """
            returns the next question from the list
        """
        current_question = self.question_list[self.question_number]
        print(current_question)
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.question_text} (True/False)?: ")