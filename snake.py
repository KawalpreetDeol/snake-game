from turtle import Turtle
# import time as Time
class Snake():
    segments = []
    def __init__(self):
        # self.segments = []
        # super().__init__()
        self.reset()
    
    def add_segment(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        # snake.shapesize(1,1)
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)
    
    def reset(self):
        for seg in self.segments:
            seg.reset()
        self.segments.clear()
        init_coord = [0, -20, -40]
        for coord in init_coord:
            self.add_segment((coord, 0))
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
    
    def up(self):
        if(self.segments[0].heading() != 270):
            self.segments[0].setheading(90)
        

    def down(self):
        if(self.segments[0].heading() != 90):
            self.segments[0].setheading(270)

    def right(self):
        if(self.segments[0].heading() != 180):
            self.segments[0].setheading(0)

    def left(self):
        if(self.segments[0].heading() != 0):
            self.segments[0].setheading(180)
