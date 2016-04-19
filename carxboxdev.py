import pygame



pygame.init()

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time

# Initialize the joysticks
pygame.joystick.init()


#def getpadevent():
global JX


def padprintout():
    name = JX.get_name()   #名字
    #axes = JX.get_numaxes()  #
    a = JX.get_axis
    #buttons = JX.get_numbuttons()
    b=JX.get_button
    #hats = JX.get_numhats()
    hat = JX.get_hat(i)

    print("Joystick {} : {} = LP[{:>6.2f},{:>6.2f}],LT[{:>6.2f}] \
    || RP[{:>6.2f},{:>6.2f}],RT[{:>6.2f}] \
    || A:{},B:{},X:{},Y:{} = LB:{},RB:{} LP:{},RP:{} \
    || BACK:{},START:{},XBOX:{} || hat: {}"\
    .format(i,name,a(0),-a(1),(a(2)+1)/2,a(3),-a(4),(a(5)+1)/2,\
    b(0),b(1),b(2),b(3),b(4),b(5),b(9),b(10),b(6),b(7),b(8), str(hat)))

# -------- Main Program Loop -----------

J_count = pygame.joystick.get_count()
for i in range(J_count):

    JX = pygame.joystick.Joystick(i)
    JX.init()
    #getpadevent()
    padprintout()

while done==False:
    clock.wait(50)
    for event in pygame.event.get(): # User did something
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        padprintout()
        if event.type == pygame.JOYBUTTONDOWN:
            if JX.get_button(8)==1: # If user clicked close    #done=True # Flag that we are done so we exit this loo
                pygame.quit()
                quit()
            elif JX.get_button(7)==1:
                print("~~~~~~start button on~~~~~~")
            elif JX.get_button(2)==1: #xboxpad X
                # go forward Lx is JX.get_axis(0)
                print("go forward Lx = {}".format(JX.get_axis(0)))
            elif JX.get_button(3)==1:
                # go forward Lx is JX.get_axis(0)
                print("backward Lx = {}".format(JX.get_axis(0)))
        if event.type == pygame.JOYBUTTONUP:
            if JX.get_button(8)==1: # If user clicked close    #done=True # Flag that we are done so we exit this loo
                pygame.quit()
                quit()
            elif JX.get_button(7)==1:
                print("~~~~~~start button off~~~~~~")
            elif JX.get_button(2)==0: #xboxpad X
                # go forward Lx is JX.get_axis(0)
                print("BREAK!!! go forward Lx = {}".format(JX.get_axis(0)))
            elif JX.get_button(3)==0:
                # go forward Lx is JX.get_axis(0)
                print("BREAK!!! backward Lx = {}".format(JX.get_axis(0)))
        #if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP or \
         #event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYHATMOTION:


            # Limit to 20 frames per second
    #clock.tick(1)


        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
