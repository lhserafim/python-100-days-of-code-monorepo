from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    # DICA. Estou atribuindo um tipo para o meu parâmetro. Isto é opcional mas ajuda no autocomplete.
    # Isto é similar ao TypeScript
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Amazon acquired Twitch in August 2014 for",
                                                     fill=THEME_COLOR,
                                                     width=280,  # width faz a quebra do texto
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.img_true = PhotoImage(file="images/true.png")
        self.img_false = PhotoImage(file="images/false.png")
        self.button_true = Button(image=self.img_true, command=self.true_pressed)
        self.button_true.grid(column=0, row=2)
        self.button_false = Button(image=self.img_false, command=self.false_pressed)
        self.button_false.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the Game")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # No caso de tkinter, não posso usar o timer, por causa do mainloop()
        self.window.after(1000, self.get_next_question)






