import serial
import pydirectinput
arduino = serial.Serial('COM5', 115200, timeout=.1)
pydirectinput.PAUSE = 0
keysDown = {}
def keyDown(key):
    keysDown[key] = True
    pydirectinput.keyDown(key)
def keyUp(key) :
    if key in keysDown:
        del(keysDown[key])
        pydirectinput.keyUp(key)


def handleJoyStickAsArrowKeys(x, y, z):
    if x == 1:
        keyDown('w')
        keyUp('s')
    elif x == 2:
        keyDown('w')
        keyUp('s')
    else:
        keyUp('up')
        keyUp('down')


    if y == 2:
        keyDown('right')
        keyUp('left')
    elif y == 0:
        keyDown('left')
        keyUp('right')
    else:
        keyUp('left')
        keyUp('right')
    if z == 1:
        keyDown('i')
    else:
        keyUp('i')

while True:
    rawdata = arduino.readline()
    data = str(rawdata.decode('utf-8'))
    if data.startswith("S"):
        dx = int(data[1])
        dy = int(data[3])
        JSButton = int(data[5])
        handleJoyStickAsArrowKeys(dx,dy,JSButton)