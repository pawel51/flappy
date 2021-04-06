from tkinter import CENTER

class ScoreLabel:
    def __init__(self, canvas):
        self.canvas = canvas
        x = int(canvas.winfo_width()/2-30)
        self.label = canvas.create_text(x, 40, justify=CENTER, text="Score: 0", font=("Consolas", 30), fill='#f7cc20', tag="score")
        self.canvas.tag_raise(self.label)
        self.score = 0

    def change_score(self, amount):
        self.score += amount
        self.canvas.itemconfig(self.label, text="Score: {}".format(self.score))
