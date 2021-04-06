from tkinter import Canvas, NW, PhotoImage, Label
from PIL import ImageTk, Image


def c_init(window, game_width, game_height):
    canvas = Canvas(window, width=game_width, height=game_height)
    canvas.pack()
    return canvas
