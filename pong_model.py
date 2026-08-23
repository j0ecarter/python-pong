from dataclasses import dataclass


@dataclass
class PongModel:
    width: int = 800
    height: int = 600
    paddle_half_height: int = 50
    ball_x: float = 0
    ball_y: float = 0
    velocity_x: float = 5
    velocity_y: float = 4
    left_y: float = 0
    right_y: float = 0
    left_score: int = 0
    right_score: int = 0

    def move_paddle(self, side: str, amount: int) -> None:
        limit = self.height / 2 - self.paddle_half_height
        attr = "left_y" if side == "left" else "right_y"
        current = getattr(self, attr)
        setattr(self, attr, max(-limit, min(limit, current + amount)))

    def reset_ball(self, toward: str) -> None:
        self.ball_x = 0
        self.ball_y = 0
        self.velocity_x = 5 if toward == "right" else -5
        self.velocity_y = 4

    def tick(self) -> str:
        self.ball_x += self.velocity_x
        self.ball_y += self.velocity_y

        if abs(self.ball_y) >= self.height / 2 - 12:
            self.velocity_y *= -1

        # paddle hit areas
        if self.ball_x <= -350 and self.velocity_x < 0 and abs(self.ball_y - self.left_y) <= self.paddle_half_height:
            self.ball_x = -350
            self.velocity_x *= -1.06
        if self.ball_x >= 350 and self.velocity_x > 0 and abs(self.ball_y - self.right_y) <= self.paddle_half_height:
            self.ball_x = 350
            self.velocity_x *= -1.06

        if self.ball_x < -self.width / 2:
            self.right_score += 1
            self.reset_ball("left")
            return "right_scored"
        if self.ball_x > self.width / 2:
            self.left_score += 1
            self.reset_ball("right")
            return "left_scored"
        return "playing"
