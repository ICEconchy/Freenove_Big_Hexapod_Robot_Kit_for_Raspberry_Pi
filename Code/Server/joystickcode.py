#Import everything in the control module, 
#including functions, classes, variables, and more.
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
Powbtn = 316
#AnalR =
#AnalL = 
CENTER_TOLERANCE = 350
zpos = 0 # initial position
#prints out device info at start
print(gamepad)
c.order=['','','','','',''] #data to be sent to control

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
            elif event.code == PowBtn
                c.order=['CMD_BUZZER', '1']
                c.condition()
                sleep(2)
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
