import re
from tkinter import PhotoImage


class Bird:
    def __init__(self, canvas, position, velocity, acceleration, diameter):
        self.pos = position
        self.vel = velocity
        self.g = acceleration
        self.dia = diameter
        self.canvas = canvas

        x0 = position
        y0 = 0.45 * canvas.winfo_width()
        x1 = x0 + diameter
        y1 = y0 + diameter
        self.entity = canvas.create_oval(x0, y0, x1, y1, fill='#f8ff2e')
        print("bird created" + str(self.canvas.coords(self.entity)))

    def move(self):
        self.vel = self.calc_vel()
        self.canvas.move(self.entity, 0, self.vel)
        if len(self.check_hitbox()) > 1:
            self.fall()
            return 0
        return 1

    def fall(self):
        self.g = 0
        self.vel = 0
        self.vel = 10

    def check_hitbox(self):
        hitbox = self.canvas.coords(self.entity)
        return self.canvas.find_overlapping(hitbox[0], hitbox[1], hitbox[2], hitbox[3])

    def jump(self, up_force, music):
        self.vel = 0
        self.vel = -up_force
        music.play_flatter()

    def calc_vel(self):
        return self.vel + self.g
