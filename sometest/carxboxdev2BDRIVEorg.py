import pygame
import RPi.GPIO as GPIO

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
Rtlim=0.005
GO=1
p=0


def restart():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
def shutdown():
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

def CMD0ini():
    ini0=1
    GPIO.output(BrkR, ini0)
    GPIO.output(TrnR, ini0)
    GPIO.output(BrkL, ini0)
    GPIO.output(TrnL, ini0)
    AcR.ChangeDutyCycle(0)
    AcL.ChangeDutyCycle(0)

def CMDpwmCD(Ar,Al): #CMDpwmCD(Ar,Al): Dr, Dl
    AcR.ChangeDutyCycle(PWMdcConstant*Ar)
    AcL.ChangeDutyCycle(PWMdcConstant*Al)

def CMDrelay(Br,Tr,Bl,Tl):  # CMDrelay(Br,Bl,Tr,Tl)
    GPIO.output(BrkR, Br)
    GPIO.output(TrnR, Tr)
    GPIO.output(BrkL, Bl)
    GPIO.output(TrnL, Tl)



BrkR=29 #Relay in4
TrnR=31 #Relay in3
BrkL=33 #Relay in2
TrnL=35 #Relay in1
AccR=18
AccL=16
outport=[BrkR,BrkL,TrnR,TrnL,AccR,AccL]
PWMfq=2500
PWMdcConstant=100

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
# Break right wheel & left wheel, on/off out
# Revers right & left wheel, on/off out
# Acc. right & left wheel, PWM out
GPIO.setup(outport, GPIO.OUT)


AcR = GPIO.PWM(AccR, PWMfq)  #100hz
AcL = GPIO.PWM(AccL, PWMfq)  #100hz
AcR.start(0)
AcL.start(0)

CMD0ini()




# -------- Main Program Loop -----------

J_count = pygame.joystick.get_count()
if J_count == 0:
    print("No Joystick and QUIT")
    pygame.quit()
    quit()

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
    if event.type==pygame.JOYBUTTONDOWN and JX.get_button(8)==1:
        GO=1
        Lx=0
        Rt=0
        Dr=0
        Dl=0
        CMD0ini


    elif event.type==pygame.JOYBUTTONDOWN and JX.get_button(7)==1:
        print("REBOOT...")
        pygame.quit()
        clock.wait(3000)
        restart()

    elif event.type==pygame.JOYBUTTONDOWN and JX.get_button(6)==1:
        print("!!SHUTDOWN!!")
        pygame.quit()
        clock.wait(3000)
        shutdown()
    elif event.type==pygame.JOYBUTTONDOWN and\
     JX.get_button(4)==1 and JX.get_button(5)==1 and JX.get_button(10)==1 :
        print("QUIT")
        pygame.quit()
        quit()


    if GO==1:
        print("start!")
        while GO==1:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    if JX.get_button(6)==1 or JX.get_button(7)==1 or JX.get_button(8)==1:
                        GO=0
                        CMD0ini
                        print("wait start command...")
                    if JX.get_button(5)==1:
                        #CMD0ini
                        CMDpwmCD(0,0)
                        CMDrelay(1,1,1,1) #break
                        break

                    # go forward Lx is JX.get_axis(0)
                    while JX.get_button(2)==1: #xboxpad X
                        event=pygame.event.get()
                        Lx = JX.get_axis(0)
                        Rt = (JX.get_axis(5)+1)/2
                        CMDrelay(0,1,0,1)  # CMDrelay(Br,Tr,Bl,Tl)
                        if JX.get_button(5)==1:
                            #CMD0ini
                            CMDpwmCD(0,0)
                            CMDrelay(1,1,1,1) #break
                        elif -Lxlim <= Lx <= Lxlim and Rt >= Rtlim :
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
                            CMDpwmCD(0,0)
                            CMDrelay(0,1,0,1) #no break
                        else:
                            Dr=0
                            Dl=0
                            CMDpwmCD(0,0)
                            CMDrelay(0,1,0,1) #no break

                        CMDpwmCD(Dr,Dl) #CMDpwmCD(Ar,Al): Dr, Dl
                        print("go forward Turn(Lx)= {:>6.2f} -- Throttle(RT) = {:>6.2f}  ===>  D Left={:>6.2f}, D Right={:>6.2f} "\
                              .format(Lx,Rt,Dl,Dr))
                        #
                        clock.wait(2)
                        if JX.get_button(5)==1:
                            #CMD0ini
                            CMDpwmCD(0,0)
                            CMDrelay(1,1,1,1) #break
                        elif JX.get_button(2)==0:
                            #CMD0ini
                            CMDpwmCD(0,0)
                            CMDrelay(1,1,1,1)
                            print("forward !!BREAK!! Turn(Lx)= {:>6.2f} -- Throttle(RT) = {:>6.2f}  ===>  D Left={:>6.2f}, D Right={:>6.2f} "\
                                  .format(Lx,Rt,Dl,Dr))

                    # go forward Lx is JX.get_axis(0)
                    while JX.get_button(3)==1:
                        event=pygame.event.get()
                        Lx = JX.get_axis(0)
                        Rt = (JX.get_axis(5)+1)/2
                        CMDrelay(0,0,0,0)  # CMDrelay(Br,Tr,Bl,Tl)
                        if JX.get_button(5)==1:
                            #CMD0ini
                            CMDpwmCD(0,0)
                            CMDrelay(1,0,1,0) #break
                        elif -Lxlim <= Lx <= Lxlim and Rt >= Rtlim :
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
                            CMDpwmCD(0,0)
                            CMDrelay(0,0,0,0) #no break
                        else:
                            Dr=0
                            Dl=0
                            CMDpwmCD(0,0)
                            CMDrelay(0,0,0,0) #no break

                        CMDpwmCD(Dr,Dl) #CMDpwmCD(Ar,Al): Dr, Dl
                        print("backward Turn(Lx)= {:>6.2f} -- Throttle(RT) = {:>6.2f}  ===>  D Left={:>6.2f}, D Right={:>6.2f} "\
                              .format(Lx,Rt,Dl,Dr))
                        #
                        clock.wait(2)
                        if JX.get_button(5)==1:
                            CMDpwmCD(0,0)
                            CMDrelay(1,0,1,0) #break
                        elif JX.get_button(3)==0:
                            CMDpwmCD(0,0)
                            CMDrelay(1,0,1,0) #break
                            print("backward !!BREAK!! Turn(Lx)= {:>6.2f} -- Throttle(RT) = {:>6.2f} ===>  D Left={:>6.2f}, D Right={:>6.2f} "\
                                  .format(Lx,Rt,Dl,Dr))
