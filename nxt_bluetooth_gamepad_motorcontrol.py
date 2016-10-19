import pygame

from nxt.locator import find_one_brick
from nxt.motor import *
from time import sleep, clock

pygame.init()

done = False

joystick_count=pygame.joystick.get_count()
if joystick_count == 0:
    print ("Error, I didn't find any joysticks.")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
 
brick = find_one_brick()
mc = brick.mc

left_engine  = Motor(brick, PORT_B)
right_engine = Motor(brick, PORT_C)
 
vehicle = SynchronizedMotors(left_engine, right_engine, 0)
 
angle = 0
angle_prev = 0

mc.start()
sleep(1)

while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    if joystick_count != 0:
     
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(3)
        button = my_joystick.get_button(0)

    angle = int(-1 * horiz_axis_pos * 45)

    speed = int(vert_axis_pos * 90)

    #print angle


    if mc.is_ready(PORT_A):
        mc.move_to(PORT_A, 30, angle, 1, 0, 0)
      
    left_engine.run(speed)
    right_engine.run(speed)
     
    if button > 0:
        done=True
    
mc.stop()
pygame.quit()

