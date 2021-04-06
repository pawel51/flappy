from tkinter import *


def w_init(window, game_width, game_height):
    window.title("Flappy Bird")
    window.resizable(False, False)
    window.iconbitmap("img/favicon.ico")
    # centralizing
    window_height = window.winfo_height()
    window_width = window.winfo_width()
    screen_width = int(window.winfo_screenwidth())
    screen_height = int(window.winfo_screenheight())
    x = int((screen_width / 2) - (game_width / 2))
    y = int((screen_height / 2) - (game_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


def bindings():
    pass
