import cv2
import urllib.request
import numpy as np
import time
import serial
import threading


# adapted from https://how2electronics.com/color-detection-tracking-with-esp32-cam-opencv/

def nothing(x):
    pass


url = 'http://10.0.0.68/cam-lo.jpg'
##'''cam.bmp / cam-lo.jpg /cam-hi.jpg / cam.mjpeg '''
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)

l_h, l_s, l_v = 128, 54, 0
u_h, u_s, u_v = 222, 149, 251
ser = serial.Serial('COM6', 9800, timeout=0.1, write_timeout=0.1)


class ConnectingToArduino:
    def __init__(self):
        self._last_func = None
        # self._firstServe = None
        self._betweensets = None

    # def firstServeChecker(self):
    #     t = threading.Timer(3, self.ThreeSecondDelay)
    #     t.start()
    #     self._firstServe = 2

    def timeBetweenSets(self):
        t = threading.Timer(17, self.delayBetweenSets)
        t.start()
        self._betweensets = 1

    def TenSecondDelay(self):
        self._last_func = None

    # def ThreeSecondDelay(self):
    #     self._firstServe = None

    def delayBetweenSets(self):
        self._betweensets = None
        ser.write(b'N')

    def detectColourPos(self):
        # SerialMonitor = ser.read(size=1)
        # print(cy)
        # print(cx)
        # if self._firstServe == 2 or self._firstServe == 0:
        #     print("First Serve")
        if self._betweensets == 1:
            print("Between Sets")
        if self._betweensets != 1:
            if 175 >= cy >= 125:
                if 75 >= cx >= 0:
                    # print(SerialMonitor)
                    # if SerialMonitor == b'9':
                    #     self._firstServe = 0
                    # else:
                    print('detected x')
                    ConnectionToC.connectionToArduinoX()
                if 315 >= cx >= 250:
                    # if SerialMonitor == b'9':
                    #     self._firstServe = 0
                    # else:
                    print('detected y')
                    ConnectionToC.connectionToArduinoY()

    def connectionToArduinoX(self):
        if self._last_func == 'connectionToArduinoX':
            print('ConnectionToArduinoX called multiple times in succession')
        else:
            ser.write(b'X')
            t = threading.Timer(2, self.TenSecondDelay)
            t.start()
            self._last_func = 'connectionToArduinoX'

    def connectionToArduinoY(self):
        if self._last_func == 'connectionToArduinoY':
            print('ConnectionToArduinoY called multiple times in succession')
        else:
            ser.write(b'Y')
            t = threading.Timer(2, self.TenSecondDelay)
            t.start()
            self._last_func = 'connectionToArduinoY'


ConnectionToC = ConnectingToArduino()


def ArduinoSerialMonitor():
    serialMonitor = ser.read(size=1)
    # print(SerialMonitor)
    if serialMonitor == b'5':
        ConnectionToC.timeBetweenSets()
    if serialMonitor == b'6':
        time.sleep(59)
    if serialMonitor == b'9':
        time.sleep(3)


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
