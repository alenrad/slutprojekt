from dictionary import *

def ball_reset():
    glo["ball_x"] = 390
    glo["ball_y"] = 290
    glo["powerup_count"] = 0
    
def powerup_remove():
    glo["powerup_x"] = -1000
    glo["powerup_y"] = -1000
    glo["counter"] = 0
    
def powerup_reset():
    glo["powerup_x"] = 400
    glo["powerup_y"] = 200
    glo["counter"] = 0
    glo["powerup_count"] = 0
    
def little_ball_reset():
    glo["little_ball_x"] = 390
    glo["little_ball_y"] = 290
    
def bounce_back_ball_left():
    glo["ball_dx"] = glo["ball_dx"] * -1
    angle_velocity = atan(glo["ball_dy"]/ glo["ball_dx"])
    angle_velocity += random(-1, 1) 
    velosity = (glo["ball_dy"]**2 + glo["ball_dx"]**2)**0.5
    glo["ball_dx"] = velosity*cos(angle_velocity)
    glo["ball_dy"] = velosity*sin(angle_velocity)

def bounce_back_ball_right():
    glo["ball_dx"] = glo["ball_dx"] * -1
    angle_velocity = atan(glo["ball_dy"]/ glo["ball_dx"])
    angle_velocity += random(-1, 1) 
    velosity = (glo["ball_dy"]**2 + glo["ball_dx"]**2)**0.5
    glo["ball_dx"] = velosity*cos(angle_velocity+PI)
    glo["ball_dy"] = velosity*sin(angle_velocity+PI)

def check_and_perform_bounce_on_paddles():
    distance_between_ball_paddle_left = (((glo["left_y"] - glo["ball_y"])**2 + (0.0 - glo["ball_x"])**2)**0.5)
    distance_between_ball_paddle_right = (((glo["right_y"] - glo["ball_y"])**2 + (800.0 - glo["ball_x"])**2)**0.5)
    perform_bounce_left = distance_between_ball_paddle_left < 75
    perform_bounce_right = distance_between_ball_paddle_right < 75
    
    if perform_bounce_left:
        bounce_back_ball_left()
        glo["counter"] += 1
        print(glo["counter"])
    if perform_bounce_right:
        bounce_back_ball_right()
        glo["counter"] += 1
        print(glo["counter"])
        
#left paddle bounce for little_ball    
    if  glo["little_ball_x"] < 40 and  glo["little_ball_y"] > glo["left_y"] and  glo["little_ball_y"] < (glo["left_y"] + 80):
        glo["right_score"] -= 2
        little_ball_reset()
            
        #right paddle bounce for little_ball  
    if  glo["little_ball_x"] > 760 and  glo["little_ball_y"] > glo["right_y"] and  glo["little_ball_y"] < (glo["right_y"] + 80):
        glo["left_score"] -= 2
        little_ball_reset()
        
def check_and_perform_collision_with_balls():
    distance_between_balls = (((glo["powerup_y"] - glo["ball_y"])**2 + (glo["powerup_x"] - glo["ball_x"])**2)**0.5)
    perform_powerup = distance_between_balls < 30
    
    if perform_powerup and glo["ball_dx"] > 0 and glo["powerup_count"] == 0:
        glo["paddle_height_left"] = 100 + 50
        glo["powerup_count"] = glo["powerup_count"] + 1
        powerup_remove()
    if perform_powerup and glo["ball_dx"] < 0:
        glo["paddle_height_right"] = 100+50
        glo["powerup_count"] = glo["powerup_count"] + 1
        powerup_remove()
    if glo["paddle_height_right"] > 100 and  glo["counter"] > 10:
            glo["paddle_height_right"] = 150-50
            powerup_reset()
    if glo["paddle_height_left"] > 100 and  glo["counter"] > 10:
        glo["paddle_height_left"] = 150-50
        powerup_reset()
        
def check_and_perform_scoring():
    #scoring - left or right side of screen
    if glo["ball_x"] > 780:
        glo["right_score"] += 1
        ball_reset()
    elif glo["ball_x"] < 0:
        glo["left_score"] += 1
        ball_reset()
        
        #winning number
    if  glo["right_score"] == 7 or  glo["left_score"] == 7:
        mode = "game-over"
        
def check_balls_bounce_off_top_or_bottom():
    #ball bounce off top / bottom
    if glo["ball_y"] > 580 or glo["ball_y"] < 0:
        glo["ball_dy"] = glo["ball_dy"] * -1
            
    #ball bounce off top / bottom
    if glo["ball_x"] > 780 or glo["ball_x"] < 0:
        glo["ball_dx"] = glo["ball_dx"] * 1   
            
    #little_ball bounce off top / bottom
    if  glo["little_ball_x"] > 780 or  glo["little_ball_x"] < 0:
        glo["little_ball_dx"] =  glo["little_ball_dx"] * -1   
            
        #little_ball bounce off top / bottom
    if  glo["little_ball_y"] > 580 or  glo["little_ball_y"] < 0:
        glo["little_ball_dy"] =  glo["little_ball_dy"] * -1 
            
        #powerup bounce off top / bottom
    if glo["powerup_x"] > 780 or glo["powerup_x"] < 0:
        glo["powerup_dx"] = glo["powerup_dx"] * -1   
            
        #powerup bounce off top / bottom
    if glo["powerup_y"] > 580 or glo["powerup_y"] < 0:
        glo["powerup_dy"] = glo["powerup_dy"] * -1 

def move_all_balls():
    #moving ball
    glo["ball_x"] = glo["ball_x"] + glo["ball_dx"]
    glo["ball_y"] = glo["ball_y"] + glo["ball_dy"]
    
    #moving little_ball ball
    glo["little_ball_x"] =  glo["little_ball_x"] +  glo["little_ball_dx"]
    glo["little_ball_y"] =  glo["little_ball_y"] +  glo["little_ball_dy"]
        
    #moving powerup ball
    glo["powerup_x"] = glo["powerup_x"] + glo["powerup_dx"] 
    glo["powerup_y"] = glo["powerup_y"] + glo["powerup_dy"] 
       
def check_if_paddle_touch_top_bottom():
    #paddle touch top/bottom
    if glo["left_y"] > 550:
        glo["left_y"] -= 6
    elif glo["left_y"] < 50:
        glo["left_y"] += 6
    elif glo["right_y"] > 550:
        glo["right_y"] -= 6
    elif glo["right_y"] < 50:
        glo["right_y"] += 6
