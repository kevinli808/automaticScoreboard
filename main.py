import cv2
import urllib.request
import numpy as np
import time
import serial
import threading

# partially adapted from https://how2electronics.com/color-detection-tracking-with-esp32-cam-opencv/

def nothing(x):
    pass

url = 'http://10.0.0.68/cam-lo.jpg'
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)

##These values represent range of the colour of the glove for detection 
l_h, l_s, l_v = 128, 54, 0
u_h, u_s, u_v = 222, 149, 251
ser = serial.Serial('COM6', 9800, timeout=0.1, write_timeout=0.1)


class ConnectingToArduino:
    def __init__(self):
        self._last_func = None
        # self._firstServe = None
        self._betweensets = None

    ##the time between sets where AutoScore will no temporarily stop detecting for colour (nothing is happening on the court)
    ##starts the timer on the scoreboard for 3 minutes
    def timeBetweenSets(self):
        t = threading.Timer(17, self.delayBetweenSets)
        t.start()
        self._betweensets = 1

    ##allows for a 10 second pause in case of an unforseen in-game error/event  
    def TenSecondDelay(self):
        self._last_func = None

    ##sends pause to Arduino Script
    def delayBetweenSets(self):
        self._betweensets = None
        ser.write(b'N')

    ##sends the current coordinates 
    def detectColourPos(self):
        ##if statement checks if there is currently a set being played (to ensure the referee is actually signalling and not doing something else)
        if self._betweensets == 1:
            print("Between Sets")
        else:
            ##there are two regions (one for each side) that the referee's hand will be in to signal for a point
            ##the left side will now be called X
            ##the right side will be called Y

            ##NOTE: DESPITE THE NAMES, X AND Y DO NOT REFER TO THE ORDERED PAIR (X,Y) USED FOR COORDS

            ##See if within specified y-axis range
            if 175 >= cy >= 125:
                ##check if within specified x-axis range for the left (X) side
                if 75 >= cx >= 0:
                    print('detected x')
                    ConnectionToC.connectionToArduinoX()
                    ##check if within specified x-axis range for the right (Y) side
                if 315 >= cx >= 250:
                    print('detected y')
                    ConnectionToC.connectionToArduinoY()

    ##The next two functions are called when the referee's hand has entered the specified region   
    def connectionToArduinoX(self):
        ##this if statement checks if the left hand region had just been called 
        if self._last_func == 'connectionToArduinoX':
            print('ConnectionToArduinoX called multiple times in succession')
        else:
            ##if if the left hand region hasn't be called, the character 'X' is sent ot the C program to reflect a scoreboard change
            ##a ten second timer is started where points cannot be registered. This accounts for the time it takes to set up a new point where the referee might move their hand into the region that detects points for reasons side from signalling 
            ser.write(b'X')
            t = threading.Timer(2, self.TenSecondDelay)
            t.start()
            self._last_func = 'connectionToArduinoX'

    def connectionToArduinoY(self):
        ##same as the left hand region but for the right
        if self._last_func == 'connectionToArduinoY':
            print('ConnectionToArduinoY called multiple times in succession')
        else:
            ser.write(b'Y')
            t = threading.Timer(2, self.TenSecondDelay)
            t.start()
            self._last_func = 'connectionToArduinoY'


ConnectionToC = ConnectingToArduino()

##read incoming numbers from buttons sent through Arduino Script
## 5 = a set just ended and there is now a 3 minute break
## 6 = a time out was just called and there is now a 1 minute break
## 9 = a point was just scored and there is a 3 second "cooldown" to allow for the next serve to be set up
def ArduinoSerialMonitor():
    serialMonitor = ser.read(size=1)
    # print(SerialMonitor)
    if serialMonitor == b'5':
        ConnectionToC.timeBetweenSets()
    if serialMonitor == b'6':
        time.sleep(59)
    if serialMonitor == b'9':
        time.sleep(3)

##sets up and reads data from camera
while True:
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgnp, -1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    ArduinoSerialMonitor()

    for c in cnts:
        area = cv2.contourArea(c)
        if area > 100:
            # min area the colour needs to be
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 3, (255, 255, 255), -1)
            cv2.putText(frame, "blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            ConnectionToC.detectColourPos()

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("live transmission", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break

cv2.destroyAllWindows()