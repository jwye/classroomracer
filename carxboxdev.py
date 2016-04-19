import pygame

pygame.init()

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time

# Initialize the joysticks
pygame.joystick.init()

#def getpadevent():
global JX,AX,BU,HA
GO=0

def padprintout():
    name = JX.get_name()   #名字
    #axes = JX.get_numaxes()  #
    a = JX.get_axis
    #buttons = JX.get_numbuttons()
    b=JX.get_button
    #hats = JX.get_numhats()
    hat = JX.get_hat(i)
    AX = a
    BU = b
    HA = hat

    print("Joystick {} : {} = LP[{:>6.2f},{:>6.2f}],  LT[{:>6.2f}]\
    || RP[{:>6.2f},{:>6.2f}],  RT[{:>6.2f}]\
    || A:{},B:{},X:{},Y:{} = LB:{},RB:{} LP:{},RP:{}\
    || BACK:{},START:{},XBOX:{}  ||  hat: {}"\
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
    if GO==1:
        print("start!")
        while GO==1:
            for event in pygame.event.get(): # User did something
                # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
                if event.type == pygame.JOYBUTTONDOWN:
                    if JX.get_button(7)==1: # If user clicked close    #done=True # Flag that we are done so we exit this loo
                        clock.wait(3000)
                        if JX.get_button(7)==1
                            print("release")
                            clock.wait(6000)
                            if JX.get_button(7)==0
                                GO=0
                    while JX.get_button(2)==1: #xboxpad X
                        # go forward Lx is JX.get_axis(0)
                        print("go forward Lx = {}".format(JX.get_axis(0)))
                        clock.wait(1000)
                        if JX.get_button(2)==0
                            print("BREAK!!! go forward Lx = {}".format(JX.get_axis(0)))


                    while JX.get_button(3)==1:
                        # go forward Lx is JX.get_axis(0)
                        print("backward Lx = {}".format(JX.get_axis(0)))
                        clock.wait(1000)
                        if JX.get_button(3)==0
                            print("BREAK!!! backward Lx = {}".format(JX.get_axis(0)))


    while GO==0:
        print("wait start command...")#padprintout()
        for event in pygame.event.get(): # User did something
            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
            if event.type == pygame.JOYBUTTONDOWN:
                if JX.get_button(8)==1: # If user clicked close    #done=True # Flag that we are done so we exit this loo
                    print("QUIT")
                    pygame.quit()
                    quit()
                elif JX.get_button(7)==1: # If user clicked close    #done=True # Flag that we are done so we exit this loo
                    clock.wait(3000)
                    if JX.get_button(7)==1
                        print("release")
                        clock.wait(6000)
                        if JX.get_button(7)==0
                            GO=1



'''
                if JX.get_button(7)==1:
                    print("~~~~~~start button on~~~~~~")
                if JX.get_button(7)==1:
                    print("~~~~~~start button off~~~~~~")

                if JX.get_button(2)==1: #xboxpad X
                    # go forward Lx is JX.get_axis(0)
                    print("go forward Lx = {}".format(JX.get_axis(0)))
                elif JX.get_button(3)==1:
                    # go forward Lx is JX.get_axis(0)
                    print("backward Lx = {}".format(JX.get_axis(0)))
                elif JX.get_button(2)==0: #xboxpad X
                    # go forward Lx is JX.get_axis(0)
                    print("BREAK!!! go forward Lx = {}".format(JX.get_axis(0)))
                elif JX.get_button(3)==0:
                    # go forward Lx is JX.get_axis(0)
                    print("BREAK!!! backward Lx = {}".format(JX.get_axis(0)))
            if event.type == pygame.JOYBUTTONUP:
                if JX.get_button(8)==1: # If user clicked close    #done=True # Flag that we are done so we exit this loo
                    pygame.quit()
                    quit()
