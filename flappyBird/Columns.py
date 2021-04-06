import random


class Columns:
    def __init__(self, canvas, number, width,
                 min_hole, max_hole, bird_diameter,
                 space_between, first_pos, x_vel):
        # create certain number of columns depending on screen width
        # randomize holes for them
        self.canvas = canvas
        self.number = number
        self.width = width
        self.height = canvas.winfo_height()
        self.game_width = canvas.winfo_width()
        self.min_hole = min_hole
        self.max_hole = max_hole
        self.bird_diameter = bird_diameter
        self.space_between = space_between
        self.first_pos = first_pos
        self.x_vel = x_vel
        self.cols_count = 0
        self.col_to_del = 0
        self.cols = []
        for i in range(number):
            self.createColumn((self.canvas.winfo_width() * self.first_pos) + self.space_between * i)


    # creates single column and translates it to right
    def createColumn(self, x1):
        y1 = random.randint(int(2 * self.bird_diameter), int(self.height - ((2 * self.bird_diameter) + self.max_hole)))
        x2 = x1 + self.width
        y2 = y1 + random.randint(self.min_hole, self.max_hole)
        higherCol = self.canvas.create_rectangle(x1, 0, x2, y1,
                                                 fill="#98ff8f", tag=f"col{self.cols_count}")
        self.canvas.tag_lower(higherCol)
        lowerCol = self.canvas.create_rectangle(x1, y2, x2, self.canvas.winfo_height(),
                                                fill="#98ff8f", tag=f"col{self.cols_count+1}")
        self.canvas.tag_lower(lowerCol)

        self.cols_count += 2
        self.cols.append([higherCol, lowerCol])
        print(self.cols)

    # moves
    def move(self, xvelocity, bird_pos, music):
        ret_flag = 0
        for cols_i in self.cols:
            self.canvas.move(cols_i[0], -xvelocity, 0)
            self.canvas.move(cols_i[1], -xvelocity, 0)
            col_back_edge = self.canvas.coords(cols_i[1])[0] + self.width
            if col_back_edge <= bird_pos <= col_back_edge+2:
                music.play_point()
                ret_flag = 1

        # if first columns went out of canvas then delete it and create new

        if self.canvas.coords(self.cols[0][0])[0] <= -self.width:
            self.cols.pop(0)

            self.canvas.delete("col{}".format(self.col_to_del))
            self.canvas.delete("col{}".format(self.col_to_del+1))
            self.col_to_del += 2
            self.createColumn(self.canvas.coords(self.cols[1][0])[0] + self.space_between)
        return ret_flag
