from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f'Score A: {self.l_score}', align="center", font=("Arial", 20, "normal"))
        self.goto(200, 260)
        self.write(f'Score B: {self.r_score}', align="center", font=("Arial", 20, "normal"))

    def l_point(self):
        if self.ycor() < 250:
            self.l_score += 1
            self.update_scoreboard()
        else:
            self.goto(self.xcor(), 250)

    def r_point(self):
        if self.ycor() > -250:
            self.r_score += 1
            self.update_scoreboard()
        else:
            self.goto(self.xcor(), -250)
