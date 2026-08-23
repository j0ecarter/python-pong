from pong_model import PongModel


def test_paddle_stays_inside_screen():
    game = PongModel()
    game.move_paddle("left", 1000)
    assert game.left_y == 250


def test_ball_bounces_off_top():
    game = PongModel(ball_y=288, velocity_y=4)
    game.tick()
    assert game.velocity_y == -4


def test_right_player_scores():
    game = PongModel(ball_x=-399, ball_y=100, velocity_x=-5)
    assert game.tick() == "right_scored"
    assert game.right_score == 1
    assert game.ball_x == 0


def test_left_paddle_bounces_ball():
    game = PongModel(ball_x=-349, ball_y=0, velocity_x=-5, left_y=0)
    game.tick()
    assert game.velocity_x > 0
