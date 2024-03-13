from questions import Questions
from tkinter import *


def answer_true():
    global score
    if next_question['correct_answer'] == 'True':
        canvas.config(bg="green")
        questions.score += 1
        score.config(text=f"Score: {questions.score}")
    else:
        canvas.config(bg="red")
    window.after(3000, pass_question)


def answer_false():
    global score
    if next_question['correct_answer'] == 'False':
        canvas.config(bg="green")
        questions.score += 1
        score.config(text=f"Score: {questions.score}")
    else:
        canvas.config(bg="red")
    window.after(3000, pass_question)


def pass_question():
    global next_question
    canvas.config(bg="white")
    next_question = questions.random_question()
    canvas.itemconfig(question, text=next_question['question'] if next_question['question'] else "Game Over!!")


questions = Questions()

window = Tk()
window.title("Quizzler")
window.config(padx=20, pady=20, bg="black")

score = Label(text=f"Score: {questions.score}", bg="black", fg="white")
score.grid(row=0, column=1)

canvas = Canvas(width=400, height=350, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=2, pady=50)

next_question = questions.random_question()
question = canvas.create_text(200, 130, width=350, text=next_question['question'], font=("Courier", 20, "bold"))

true = PhotoImage(file="./images/true.png")
false = PhotoImage(file="./images/false.png")
true_button = Button(image=true, cursor="hand2", command=answer_true)
true_button.grid(row=2, column=0)
false_button = Button(image=false, cursor="hand2", command=answer_false)
false_button.grid(row=2, column=1)

window.mainloop()
