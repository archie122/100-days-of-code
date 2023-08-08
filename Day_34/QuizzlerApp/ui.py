from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.score = 0

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label1
        self.label1 = Label(text=f"Score : {self.score}", fg="white", bg=THEME_COLOR)
        self.label1.grid(row=0, column=1)

        # Box

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.label2 = self.canvas.create_text(150, 125, text="Something", width=250, font=("Ariel", 20, "italic"),
                                              fill="black")

        # Button1

        self.button_image_1 = PhotoImage(file="images/true.png")
        self.button_1 = Button(image=self.button_image_1, highlightthickness=0, command=self.true_pressed)
        self.button_1.grid(row=3, column=0)

        # Button2

        self.button_image_2 = PhotoImage(file="images/false.png")
        self.button_2 = Button(image=self.button_image_2, highlightthickness=0, command=self.false_pressed)
        self.button_2.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label1.config(text=f"Score : {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.label2, text=q_text)
        else:
            self.canvas.itemconfig(self.label2, text=f"You've completed the quiz. Your final score is: {self.score}/{self.quiz.question_number}")
            self.button_1.config(state="disabled")
            self.button_2.config(state="disabled")

    def true_pressed(self):
        self.is_correct(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.is_correct(self.quiz.check_answer("False"))

    def is_correct(self, check_answer):
        if check_answer:
            self.canvas.config(bg="green")
            self.score += 1
            self.canvas.itemconfig(self.label2, text="You got it right!")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.label2, text="You got it wrong!")
        self.window.after(1000, self.get_next_question)

