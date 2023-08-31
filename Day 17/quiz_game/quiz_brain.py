class QuizBrain:

    # definition of the constructor
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        """
            returns whether question list is empty or not
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
            returns the next question from the list
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_guess = input(f"Q.{self.question_number}: {current_question.question_text} (True/False)?: ")
        self.check_answer(current_question.question_answer, user_guess)

    def check_answer(self, actual_answer, user_answer):
        """
            checks the user answer with the actual answer
        """
        if actual_answer.lower() == user_answer.lower():
            self.score += 1
            print("You got it right!!")
        else:
            print("That's wrong!!")
        print(f"The correct answer was: {actual_answer}")
        print(f"The current score is: {self.score}/{self.question_number}")
        print("\n")