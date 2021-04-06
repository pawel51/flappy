from tkinter import *
from canvas_init import c_init
from window_init import w_init
from Columns import *
from Bird import *
from music import MusicMixer
from ScoreLabel import *
import time

# window constants
GAME_WIDTH = 800
GAME_HEIGHT = 700

# column constants
COL_WIDTH = 100
BIRD_DIAMETER = 50
HOLE_MIN = 200
HOLE_MAX = 300
TOTAL_COLUMNS = 3
SPACE_BETWEEN = 400
WAIT_TIME = 9
FIRST_COLUMN_POS = 0.75
XVELOCITY = 3

# bird constants
G = 0.2
F = 7
VEL_Y = 0
POS_X_BIRD = FIRST_COLUMN_POS * GAME_WIDTH - SPACE_BETWEEN
DIAMETER = 40
AIR_RES = 1

# Game logi variables
GAME_OVER = 0


def make_bindings(window, bird, music):
    return window.bind("<space>", lambda event: bird.jump(F, music))


def game_over(window, canvas, bind1_id, score):

    x = int(canvas.winfo_width() / 2)
    canvas.create_text(x, 150, justify=CENTER, text="Game Over",
                                font=("Consolas", 50), fill='#9e062a', tag="game_over")
    canvas.create_text(x, 300, justify=CENTER, text="Your Score: {}".format(score),
                                font=("Consolas", 40), fill='#d92750', tag="game_over")
    canvas.tag_raise("game_over")
    canvas.delete("score")


def game_loop(window, columns0, bird, music, label, bind1_id, canvas):
    global GAME_OVER
    if(GAME_OVER == 0):
        if columns0.move(XVELOCITY, POS_X_BIRD, music):
            label.change_score(1)

    if bird.move() == 0:
        GAME_OVER = 1
        window.unbind("<space>")

        game_over(window, canvas, bind1_id, label.score)
    window.after(WAIT_TIME, game_loop, window, columns0, bird, music, label, bind1_id, canvas)


def init():
    window = Tk()

    canvas = c_init(window, GAME_WIDTH, GAME_HEIGHT)
    window.update()
    w_init(window, GAME_WIDTH, GAME_HEIGHT)

    window.update()

    columns0 = Columns(canvas, TOTAL_COLUMNS, COL_WIDTH,
                       HOLE_MIN, HOLE_MAX, BIRD_DIAMETER,
                       SPACE_BETWEEN, FIRST_COLUMN_POS, XVELOCITY)

    bird = Bird(canvas, POS_X_BIRD, VEL_Y, G, DIAMETER)

    label = ScoreLabel(canvas)

    music = MusicMixer()

    bind1_id = make_bindings(window, bird, music)
    window.bind("<KP_Enter>", lambda event: init())
    game_loop(window, columns0, bird, music, label, bind1_id, canvas)

    window.bind("<KP_Enter>", init)

    window.mainloop()


init()
