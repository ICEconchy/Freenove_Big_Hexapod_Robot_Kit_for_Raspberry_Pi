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
#Moving direction: x='0',y='25'
#Delay:'10'
#Action Mode : '0'   Angleless turn 

gamepad = InputDevice('/dev/input/event0') #creates object 'gamepad' to store the data
LeftJoy = ["", "", "", ""]

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
zpos = 20 # initial position
val = 0 # inital value
ABS_RZ = 0 # inital Lanalog
ABS_Z = 0

    
#prints out device info at start
print(gamepad)
c.order=['','','','','',''] #data to be sent to control

def setuppositions():
    print('Set up inital position')
    c.order=['CMD_HEAD',headxpos,headypos]
    c.order=['CMD_POSITION','0','0', zpos]
    c.condition()

def map(self,value,fromLow,fromHigh,toLow,toHigh):
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

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
        print('I got here ',event)
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
            
        elif absevent.event.code == 1 and absevent.event.value < ABS_RZ:
            LeftJoy[0] = absevent.event.value
            print("ABS_RZ", absevent.event.value)
        if ecodes.bytype[absevent.event.type][absevent.event.code] == ABS_Z: 
            LeftJoy[1] = absevent.event.value
            print("ABS_Z", absevent.event.value)
            if last["ABS_RZ"] > 128: 
                print('reverse')
                print (last["ABS_RZ"]) 
            elif last["ABS_RZ"] < 127: 
                print ('forward') 
                print (last["ABS_RZ"]) 
            if last["ABS_Z"] > 128 : 
                print ('right')
                print (last["ABS_Z"])
            elif last["ABS_Z"] < 127: 
                print ('left')
                print (last["ABS_Z"])