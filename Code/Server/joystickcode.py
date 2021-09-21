#Import everything in the control module, 
#including functions, classes, variables, and more.
import time
from Control import *
from evdev import list_devices, InputDevice, categorize, ecodes, KeyEvent

#Creating object 'control' of 'Control' class.
c=Control()
c.order=['','','','','','']
#example:
#data=['CMD_MOVE', '1', '0', '25', '10', '0']
#Move command:'CMD_MOVE'
#Gait Mode: "1"
#Moving direction: x='0',y='25' val = speed
#Delay:'10'
#Action Mode 1 No Angle eg left or right if set to 2 then angle 

gamepad = InputDevice('/dev/input/event0') #creates object 'gamepad' to store the data
LeftJoy = [ 0,0,0,0]

#button codes
aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308
LB = 310
RB = 311
SelBtn = 314 # gamepad select button
StBtn = 315 # gamepad start button
PowBtn = 316 # gamepad power button
LangBtn = 317
RangBtn = 318
# Left Buttons
# f,r,l,r btn rel code 17, type 03, val 00
# fwd btn code 17, type 03, val -1
# rev btn code 17, type 03, val 01
# ctn code 17, type 03, val -1
# lt btn code 16, type 03, val -1
# rt btn code 16, type 03, val 01
# ctn code 16, type 03, val 00

# Left Analog
# fwd code 01, type 03, val -32768
# rev code 01, type 03, val 32767
# ctn code 01, type 03, val -1
# lt code 00, type 03, val -32768
# rt code 00, type 03, val 32767
# ctn code 00, type 03, val -1

# Right Analog
# fwd code 04, type 03, val -32768
# rev code 04, type 03, val 32767
# ctn code 04, type 03, val -1
# lt code 03, type 03, val -32768
# rt code 03, type 03, val 32767
# ctn code 03, type 03, val 00

# bottom Left Analog
# Full press code 02, type 03, val 255
# off code 02, type 03, val 00

# bottom Right Analog
# Full press code 05, type 03, val 255
# off code 05, type 03, val 00

headxpos = 67 # initial position
headypos = 67 # initial position
headmaxypos = 179
headminypos = 1
headmaxxpos = 155
headminxpos = 53
joymaxypos = 0
joyminypos = 0
joymaxxpos = 0
joyminxpos = 0
anglemaxypos = 0
angleminypos = 0
anglemaxxpos = 0
angleminxpos = 0

zpos = 20 # initial position
val = 0 # inital value
ljx = 0 # inital Lanalog
ljy = 0
angle = 0
fixedangle_flag = 0
ABS_RX = 0
ABS_RY = 0
Joycontrolangle = 0
    
#prints out device info at start
print(gamepad)
c.order=['','','','','',''] #data to be sent to control

def setuppositions():
    print('Set up inital position')
    c.order=['CMD_HEAD',headxpos,headypos]
    c.order=['CMD_POSITION','0','0', zpos]
    c.condition()

def setanglepositions():
    if fixedangle_flag == 1:
        angle = 0
    else:
        if ljx!=0 or ljy!=0:
            print('ljx =',ljx, 'ljy =',ljy)
            angle = math.degrees(math.atan2(ljx,ljy)) # calc angle
            print('Angle atan ',angle)
            if angle < -90 and angle >= -180:
                angle=angle+360
                print('Angle neg ',angle)
            if angle >= -90 and angle <=90:
                print('Angle pos ',angle)
                angle = c.map(angle,-90,90,-10,10)
                angle = round(angle) # round up angle
            else:
                angle = c.map(angle, 270, 90, 10, -10)
                angle = round(angle) # round up angle
                print('Degree angle = ',angle)
        else:
            angle = 0
            print('Degree angle = ',angle)
            
setuppositions()

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
            if event.value == 1:
                print('JoyPad check',event.code)
            if event.code == yBtn:
                for i in range(3):
                    c.order=['CMD_MOVE', '1', '0', '35', '10', '0']
                    c.condition()
                    print('Y Button Pressed')
                else:
                    time.sleep(1)
                    c.order=['CMD_POSITION','0','0', zpos]
                    c.condition()
            elif event.code == bBtn:
                for i in range(3):
                    c.order=['CMD_MOVE', '1', '35', '0', '10', '0']
                    c.condition()
                    print('B Button Pressed')
                else:
                    time.sleep(1)
                    c.order=['CMD_POSITION','0','0', zpos]
                    c.condition()
            elif event.code == aBtn:
                for i in range(3):
                    c.order=['CMD_MOVE', '1', '0', '-35', '10', '0']
                    c.condition()
                    print('A Button Pressed')
                else:
                    time.sleep(1)
                    c.order=['CMD_POSITION','0','0', zpos]
                    c.condition()
            elif event.code == xBtn:
                for i in range(3):
                    c.order=['CMD_MOVE', '1', '-35', '0', '10', '0']
                    c.condition()
                    print('X Button Pressed')
                else:
                    time.sleep(1)
                    c.order=['CMD_POSITION','0','0', zpos]
                    c.condition()
            elif event.code == PowBtn:
                c.order=['CMD_BUZZER', '1']
                c.condition()
                time.sleep(1)
                c.order=['CMD_BUZZER', '0']
                c.condition()
            elif event.code == LB:
                if zpos < -19:
                    zpos = -20
                else:
                    zpos = zpos -2 
                c.order=['CMD_POSITION','0','0', zpos]
            #    print(zpos)
                c.condition()
            #    print('LB Button Pressed')
            elif event.code == RB:
                if zpos > 49: 
                    zpos = 50
                else:
                    zpos = zpos +2
                c.order=['CMD_POSITION','0','0', zpos]
           #     print(zpos)
                c.condition()
           #     print('RB Button Pressed')
                
#for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS: 
        absevent = categorize(event)
      #  print('I got here ',event)
        if absevent.event.code == 17 and absevent.event.value == -1 and headxpos < headmaxxpos:
            print('val = ',val)
            print('event code 17 Up')
            headxpos = headxpos +2 
            c.order=['CMD_HEAD',headxpos,headypos]
            print(headxpos,headypos)
            c.condition()
            
        elif absevent.event.code == 17 and absevent.event.value == 1:
            print('event code 17 Down')
            headxpos = headxpos -2 
            c.order=['CMD_HEAD',headxpos,headypos]
            print(headxpos,headypos)
            c.condition()
        
        elif absevent.event.code == 16 and absevent.event.value == -1:
            print('val = ',val)
            print('event code 16 Left')
            headypos = headypos +2 
            c.order=['CMD_HEAD',headxpos,headypos]
            print(headxpos,headypos)
            c.condition()
            
        elif absevent.event.code == 16 and absevent.event.value == 1:
            print('event code 16 Right')
            headypos = headypos -2 
            c.order=['CMD_HEAD',headxpos,headypos]
            print(headxpos,headypos)
            c.condition()           
    
        elif absevent.event.code == 1:
            LeftJoy[0] = absevent.event.value / 100
            print("ABS_LX", LeftJoy[0])
            ljx = round(c.map(LeftJoy[0],-328,328,35,-35))
            setanglepositions()
            print('ljx = ',ljx)
            c.order=['CMD_MOVE', '1', ljx, '0', '10',angle]
            c.condition()
        
        if absevent.event.code == 0: 
            LeftJoy[1] = absevent.event.value / 100
            print("ABS_LY", LeftJoy[1])
            ljy = round(c.map(LeftJoy[1],-328,328,35,-35))
            setanglepositions()
            print('ljy = ',ljy)
            c.order=['CMD_MOVE', '1', '0', ljy, '10',angle]
            c.condition()
           