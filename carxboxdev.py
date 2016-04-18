import pygame
import os, sys
import time
#＃＃＃也不太知道的
from os import popen
from sys import stdin
import smbus
import RPi.GPIO as GPIO
import re
#也不太知道的


pygame.init()

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()



def padprintout():
# Get count of joysticks
    J_count = pygame.joystick.get_count()
    for i in range(J_count):
        JX = pygame.joystick.Joystick(i)
        JX.init()
        print("Joystick {}".format(i) )
        # Get the name from the OS for the controller/joystick
        name = JX.get_name()   #名字
        print("Joystick name: {}".format(name) )
    ##############################################################################
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = JX.get_numaxes()  #
        print("Number of axes: {}".format(axes) )
        a = JX.get_axis
        print("LP{},RP{},RT{},LT{}"
        .format(str(a(0,1)),str(a(2,3)),a(4),a(5))
    ##############################################################################
        #get buttons
        buttons = JX.get_numbuttons()
        print("Number of buttons: {}".format(buttons) )
        b=JX.get_button
        print("A:{},B:{},X:{},Y:{},LB:{},RB:{},BACK:{},START:{},XBOX:{},LP:{},RP:{}"
        .format(b(0),b(1),b(2),b(3),b(4),b(5),b(6),b(7),b(8),b(9),b(10)) )
    #############################################################################
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = JX.get_numhats()
        print("Number of hats: {}".format(hats) )
        for i in range( hats ):
            hat = JX.get_hat( i )
            print("Hat {} value: {}".format(i, str(hat)) )
    #################################################################
        if JX.get_button(8)==1: # If user clicked close
            #done=True # Flag that we are done so we exit this loop
            pygame.quit()
            quit()

# -------- Main Program Loop -----------
padprintout()

while done==False:

    for event in pygame.event.get(): # User did something
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        padprintout()
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")


    # Limit to 20 frames per second
    clock.tick(3)


        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
