import pygame as pg


class MusicMixer:
    def __init__(self):
        pg.mixer.init()

    def play_music(self):
        pass

    def play_point(self):
        if pg.mixer.get_init() is None:
            pg.mixer.init()
        plus_one = pg.mixer.Sound("music/plus_one.wav")
        plus_one.play()

    def play_flatter(self):
        if pg.mixer.get_init() is None:
            pg.mixer.init()

        flatter = pg.mixer.Sound("music/flutter.wav")
        flatter.play()