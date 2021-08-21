#Import everything in the control module, 
#including functions, classes, variables, and more.
from Control import *
from evdev import InputDevice, categorize, ecodes


#Creating object 'control' of 'Control' class.
c=Control()

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

#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == yBtn:
                for i in range(3):
                    data=['CMD_MOVE', '1', '0', '35', '10', '0']
                    c.run(data)
                    print('y')
            elif event.code == bBtn:
                for i in range(3):
                    data=['CMD_MOVE', '1', '35', '0', '10', '0']
                    c.run(data)
                    print('b')
            elif event.code == aBtn:
                for i in range(3):
                    data=['CMD_MOVE', '1', '0', '-35', '10', '0']
                    c.run(data)
                    print('a')
            elif event.code == xBtn:
                for i in range(3):
                    data=['CMD_MOVE', '1', '-35', '0', '10', '0']
                    c.run(data)
                    print('x')
            elif event.code == LB:
                for i in range(3):
                    data=['CMD_POSITION', '0', '0', '-2']
                    c.run(data)
                    print('lb')
            elif event.code == RB:
                for i in range(3):
                    data='CMD_POSITION#0#0#20'
                    c.run(data)
                    print('rb')