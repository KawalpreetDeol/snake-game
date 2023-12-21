from turtle import Turtle

class Scoreboard(Turtle):
    score = 0
    high_score = 0
    def __init__(self):
        super().__init__()
        self.read_file()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.display_score()

    # def display_score(self):
    #     self.write(f'Score: {self.score}', False, align="center", font=("Courier", 24,"normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f'GAME OVER', False, align="center", font=("Courier", 24,"normal"))

    def read_file(self):
        try:
            with open('data.text', 'r') as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
    
    def write_file(self):
        with open('data.text', 'w') as file:
            file.write(str(self.high_score))

    def display_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, align="center", font=("Courier", 24,"normal"))
    
    def increment_score(self):
        self.score+=1
        self.clear()
        self.display_score()
    
    def refresh_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()
        self.score = 0
        # self.clear()
        self.display_score()