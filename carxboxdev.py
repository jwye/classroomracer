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
global Lx
global Rt
Dr=00
Dl=00
Cf=1  # Cf is constant for  Rt,
Ct=0.6  # Ct is for Lx turning,
Cc=1   # center calibr
Lxlim=0.12
Rtlim=0.01
GO=0
p=0


def restart():
    command = "/usr/bin/sudo /sbin/shutdown now"  #reboot "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)


def padprintout():
    name = JX.get_name()   #名字
    #axes = JX.get_numaxes()  #
    a = JX.get_axis
    #buttons = JX.get_numbuttons()
    b=JX.get_button
    #hats = JX.get_numhats()
    hat = JX.get_hat(i)

    print("Joystick {} : {} = LP[{:>6.2f},{:>6.2f}],  LT[{:>6.2f}] || RP[{:>6.2f},{:>6.2f}],  RT[{:>6.2f}] || A:{},B:{},X:{},Y:{} = LB:{},RB:{} LP:{},RP:{} || BACK:{},START:{},XBOX:{}  ||  hat: {}"\
    .format(i,name,a(0),-a(1),(a(2)+1)/2,a(3),-a(4),(a(5)+1)/2,\
    b(0),b(1),b(2),b(3),b(4),b(5),b(9),b(10),b(6),b(7),b(8), str(hat)))




# -------- Main Program Loop -----------

J_count = pygame.joystick.get_count()
for i in range(J_count):

    JX = pygame.joystick.Joystick(i)
    JX.init()
    Lx=0
    Rt=0
    #getpadevent()
    padprintout()
print("wait start command...")

while done==False:
    event=pygame.event.wait()
    print("wait...{}".format(p))
    p+=1
    if event.type==pygame.JOYBUTTONDOWN and JX.get_button(7)==1:
        GO=1
        Lx=0
        Rt=0
        Dr=0
        Dl=0

    elif event.type==pygame.JOYBUTTONDOWN and JX.get_button(8)==1: # If user clicked close    #done=True # Flag that we are done so we exit this loo
        print("now is SHUTDOWN") #time  REBOOT...")
        pygame.quit()
        clock.wait(3000)
        restart()

    elif event.type==pygame.JOYBUTTONDOWN and JX.get_button(6)==1: # If user clicked close    #done=True # Flag that we are done so we exit this loo
        print("QUIT")
        pygame.quit()
        quit()


    if GO==1:
        print("start!")
        while GO==1:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    if JX.get_button(7)==1 or JX.get_button(8)==1 or JX.get_button(6)==1:
                        GO=0
                        print("wait start command...")
                        break

                    # go forward Lx is JX.get_axis(0)
                    while JX.get_button(2)==1: #xboxpad X
                        event=pygame.event.get()
                        Lx = JX.get_axis(0)
                        Rt = (JX.get_axis(5)+1)/2
                        if -Lxlim <= Lx <= Lxlim and Rt >= Rtlim :
                            Dr=Cf*Rt
                            Dl=Cc*Dr
                        elif Lx < -Lxlim and Rt >= Rtlim :#turn left
                            Dr=(Cf*Rt)
                            Dl=(Cf*Rt)-(Cf*Rt*Ct*abs(Lx))
                        elif Lx > Lxlim and Rt >= Rtlim :#turn right
                            Dr=(Cf*Rt)-(Cf*Rt*Ct*abs(Lx))
                            Dl=(Cf*Rt)
                        elif Rt < Rtlim:
                            Dr=0
                            Dl=0
                        print("go forward Turn(Lx)= {:>6.2f} -- Throttle(RT) = {:>6.2f}  ===>  D Left={:>6.2f}, D Right={:>6.2f} "\
                              .format(Lx,Rt,Dl,Dr))
                        #
                        clock.wait(20)
                        if JX.get_button(2)==0:

                            print("forward !!BREAK!! Turn(Lx)= {:>6.2f} -- Throttle(RT) = {:>6.2f}  ===>  D Left={:>6.2f}, D Right={:>6.2f} "\
                                  .format(Lx,Rt,Dl,Dr))

                    # go forward Lx is JX.get_axis(0)
                    while JX.get_button(3)==1:
                        event=pygame.event.get()
                        Lx = JX.get_axis(0)
                        Rt = (JX.get_axis(5)+1)/2
                        if -Lxlim <= Lx <= Lxlim and Rt >= Rtlim :
                            Dr=Cf*Rt
                            Dl=Cc*Dr
                        elif Lx < -Lxlim and Rt >= Rtlim :#turn left
                            Dr=(Cf*Rt)
                            Dl=(Cf*Rt)-(Cf*Rt*Ct*abs(Lx))
                        elif Lx > Lxlim and Rt >= Rtlim :#turn right
                            Dr=(Cf*Rt)-(Cf*Rt*Ct*abs(Lx))
                            Dl=(Cf*Rt)
                        elif Rt < Rtlim:
                            Dr=0
                            Dl=0
                        print("backward Turn(Lx)= {:>6.2f} -- Throttle(RT) = {:>6.2f}  ===>  D Left={:>6.2f}, D Right={:>6.2f} "\
                              .format(Lx,Rt,Dl,Dr))
                        #
                        clock.wait(20)
                        if JX.get_button(3)==0:

                            print("backward !!BREAK!! Turn(Lx)= {:>6.2f} -- Throttle(RT) = {:>6.2f} ===>  D Left={:>6.2f}, D Right={:>6.2f} "\
                                  .format(Lx,Rt,Dl,Dr))
