from dictionary import *

def left_winner_visuals():
    text("Left player wins", 100, 300)
    text("Press (r) to restart", 100, 350)
    
def right_winner_visuals():
    text("Right player wins", 500, 300)
    text("Press (r) to restart", 500, 350)

def visual_instruction_screen():
    textSize(30)
    text("Crazy Pong", 310 , 50)
    text("Press any key to start game", 200 , 300)
    text("P1", 50 , 50)
    text("(W/S)", 30 , 90)
    text("P2", 720 , 50)
    text("(I/K)", 705 , 90)
    text("First to 7", 330 , 550)
    
def visuals_game_over(glo):
    fill(255)
    textSize(28)
    text(glo["right_score"], 350, 40)
    text(glo["left_score"], 430, 40)
        
    #paddles
    fill(255)
    arc(10, glo["left_y"], 100, glo["paddle_height_left"], -HALF_PI, HALF_PI)
    arc(790, glo["right_y"], 100, glo["paddle_height_right"], HALF_PI,TWO_PI-HALF_PI)

    #ball
    fill(255)
    ellipse(glo["ball_x"],glo["ball_y"],20,20)
    
    #little_ball
    fill(255, 51, 51)
    ellipse(glo["little_ball_x"], glo["little_ball_y"],5,5)
    
    #powerup ball
    fill(124,252,0)
    ellipse(glo["powerup_x"], glo["powerup_y"], 50, 50)
    
    #line in middle
    fill(255)
    line(400, 800, 400, 0)
    stroke(255)
def visuals_keys_game_over(glo):
    if glo["left_key"] == "w":
        glo["left_y"] += -6
    if glo["left_key"] == "s":
        glo["left_y"] += 6
    if glo["right_key"] == "i":
        glo["right_y"] += -6
    if glo["right_key"] == "k":
        glo["right_y"] += 6
