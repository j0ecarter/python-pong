import turtle

from pong_model import PongModel


def main() -> None:
    # window first
    screen = turtle.Screen()
    screen.setup(820, 650)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    model = PongModel()

    def make_paddle() -> turtle.Turtle:
        paddle = turtle.Turtle("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        return paddle

    left = make_paddle()
    right = make_paddle()
    ball = turtle.Turtle("circle")
    ball.color("white")
    ball.penup()
    score = turtle.Turtle()
    score.color("white")
    score.penup()
    score.hideturtle()
    score.goto(0, 255)

    def move(side: str, amount: int) -> None:
        model.move_paddle(side, amount)

    def tick() -> None:
        model.tick()
        left.goto(-370, model.left_y)
        right.goto(370, model.right_y)
        ball.goto(model.ball_x, model.ball_y)
        score.clear()
        score.write(f"{model.left_score}     {model.right_score}", align="center", font=("Arial", 28, "normal"))
        screen.update()
        screen.ontimer(tick, 16)

    screen.listen()
    screen.onkey(lambda: move("left", 30), "w")
    screen.onkey(lambda: move("left", -30), "s")
    screen.onkey(lambda: move("right", 30), "Up")
    screen.onkey(lambda: move("right", -30), "Down")
    tick()
    screen.mainloop()


if __name__ == "__main__":
    main()
