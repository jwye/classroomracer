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
    print("wait start command...")
    event=pygame.event.wait(JOYBUTTONDOWN)
    if event.type==pygame.JOYBUTTONDOWN and JX.get_button(7)==1:
        GO=1
    elif event.type==pygame.JOYBUTTONDOWN and JX.get_button(8)==1: # If user clicked close    #done=True # Flag that we are done so we exit this loo
        print("QUIT")
        pygame.quit()
        quit()

    if GO==1:
        print("start!")
        while GO==1:
            event=pygame.event.get()
            if event.type == pygame.JOYBUTTONDOWN:
                if JX.get_button(7)==1: # If user clicked close    #done=True # Flag that we are done so we exit this loo
                        GO=0
                        break
                # go forward Lx is JX.get_axis(0)
                while JX.get_button(2)==1: #xboxpad X
                    print("go forward Lx = {} RT = {}"\
                          .format(JX.get_axis(0),JX.get_axis(5)))
                    clock.wait(500)
                    if JX.get_button(2)==0:
                        print("BREAK!!! forward Lx = {} RT = {}"\
                              .format(JX.get_axis(0),JX.get_axis(5)))

                # go forward Lx is JX.get_axis(0)
                while JX.get_button(3)==1:
                    print("backward Lx = {} RT = {}"\
                          .format(JX.get_axis(0),JX.get_axis(5)))
                    clock.wait(500)
                    if JX.get_button(3)==0:
                        print("BREAK!!! backward Lx = {} RT = {}"\
                              .format(JX.get_axis(0),JX.get_axis(5)))
