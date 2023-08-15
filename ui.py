from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score:{self.score}", bg=THEME_COLOR, font=("Arial", 15, "normal"), fg="white")
        self.score_label.grid(column=2, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Questions Go Here!",
                                                     font=("Arial", 20, "italic"),
                                                     width=280,
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.checkmark_pic = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.checkmark_pic, highlightthickness=0, command=self.correct_answer)
        self.true_button.grid(column=0, row=2)

        self.wrong_pic = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.wrong_pic, highlightthickness=0, command=self.wrong_answer)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Gets the question to appear in the canvas."""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="This is the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct_answer(self):
        """Checks if the answer was correct."""
        is_true = self.quiz.check_answer(user_answer="True")
        self.feedback(is_true)

    def wrong_answer(self):
        """Checks if the answer was wrong."""
        is_false = self.quiz.check_answer(user_answer="False")
        self.feedback(is_false)

    def feedback(self, is_true):
        """Gives the player feedback if the answer was right or wrong."""
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

