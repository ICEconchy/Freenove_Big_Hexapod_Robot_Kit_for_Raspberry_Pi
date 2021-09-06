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

CENTER_TOLERANCE = 350
zpos = 0 # initial position
#prints out device info at start
print(gamepad)
c.order=['','','','','',''] #data to be sent to control

def map(self,value,fromLow,fromHigh,toLow,toHigh):
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            print('JoyPad check',event.code)
            if event.code == yBtn:
                for i in range(3):
                    order=['CMD_MOVE', '1', '0', '35', '10', '0']
                    c.condition()
                    print('Y Button Pressed')
            elif event.code == bBtn:
                for i in range(3):
                    order=['CMD_MOVE', '1', '35', '0', '10', '0']
                    c.condition()
                    print('B Button Pressed')
            elif event.code == aBtn:
                for i in range(3):
                    c.order=['CMD_MOVE', '1', '0', '-35', '10', '0']
                    c.condition()
                    print('A Button Pressed')
            elif event.code == xBtn:
                for i in range(3):
                    c.order=['CMD_MOVE', '1', '-35', '0', '10', '0']
                    c.condition()
                    print('X Button Pressed')
            elif event.code == PowBtn:
                c.order=['CMD_BUZZER', '1']
                c.condition()
                time.sleep(2)
                c.order=['CMD_BUZZER', '1']
                c.condition
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
                if zpos > 19: 
                    zpos = 20
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
        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RZ':
           translation = {97: None, 98: None, 99: 105}
           if absevent.event.value > 128: 
                print ('reverse') 
                print (absevent.event.value) 
           elif absevent.event.value < 127:
                print ('forward') 
                print (absevent.event.value) 
        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z':
            if absevent.event.value > 128 : 
                print ('right') 
                print (absevent.event.value) 
            elif absevent.event.value < 127: 
                print ('left') 
                print (absevent.event.value)
