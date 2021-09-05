#Import everything in the control module, 
#including functions, classes, variables, and more.
from Control import *
from evdev import InputDevice, categorize, ecodes


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

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#button code variables (change to suit your device)
aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308
LB = 310
RB = 311

zpos = 10
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
            elif event.code == LB:
                for i in range(1):
                    c.order=['CMD_POSITION','0','0','-10']
                    c.condition()
                    print('LB Button Pressed')
            elif event.code == RB:
               # for i in range(1):
                 #   zpos = zpos +1
                    c.order=['CMD_POSITION','0','0','11']
                    c.condition()
                    print('RB Button Pressed')