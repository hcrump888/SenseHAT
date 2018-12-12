from sense_hat import SenseHat
sense = SenseHat()

from time import sleep

white = (255, 255, 255)

blue = (0, 0, 255)

bat_y = 4

ball_position = [3, 3]
ball_velocity = [1, 1]

def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)

draw_bat()

def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1

sense.clear(0, 0, 0)

def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], blue)

while True:
    draw_bat()
    sense.stick.direction_up = move_up
    sleep(0.25)
    draw_ball()




























