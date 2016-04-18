import pygame
import os, sys
import time


pygame.init()

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()


# -------- Main Program Loop -----------
while Hold==False
while done==False:

# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        # Get count of joysticks
        J_count = pygame.joystick.get_count()
        i=0
    #for i in range(J_count):
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
        for i in range( axes ):
            axis = JX.get_axis( i )
            print("Axis {} value: {:>6.3f}".format(i, axis) )
    ##############################################################################
        #get buttons
        buttons = JX.get_numbuttons()
        print("Number of buttons: {}".format(buttons) )
        for i in range( buttons ):
            button = JX.get_button( i )
            print("Button {:>2} value: {}".format(i,button) )
    #############################################################################
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = JX.get_numhats()
        print("Number of hats: {}".format(hats) )
        for i in range( hats ):
            hat = JX.get_hat( i )
            print("Hat {} value: {}".format(i, str(hat)) )
    ##################################################################
        if JX.get_button(8)==1:
            done=True
        # Limit to 20 frames per second

        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
pygame.quit()
quit()
