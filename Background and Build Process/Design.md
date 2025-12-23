### **Design**
&nbsp;	This project is divided into two parts—C++ and Python. C++ is used to interact with the Arduino Uno, the scoreboard, and the buttons whilst Python is used for image processing. The two programs can communicate through the Arduino IDE’s serial monitor. This machine requires three programs for set up, two in C++ and one in Python, and requires one Python program to run.



##### **ESP32 CAM Set-Up**

&nbsp;	The first program, coded in C++, is responsible for setting up the camera’s live stream using a web server, which runs over the location’s Wi-Fi network. The code on lines 5 and 6 only ever needs to be changed when the Wi-Fi network the camera is being used on changes, otherwise, the code is stored in the ESP-32 camera.



##### **Colour Picker**

&nbsp;	The second program, coded in Python, is responsible for taking the live stream from the first program and helping the user find the LH, LS, LV, UH, US, and UV values of a specific colour. The user will be finding the colour of gloves that the referee is wearing. *It is required that the referee wears gloves* since many skin tones are commonly seen in modern-day society, which can lead to the program mistaking colours in the background of the volleyball court as points. Therefore, the glove colour must be a colour uncommonly seen in everyday life, such as purple or bright orange. 

&nbsp;	When run, the program will show the live stream as well as six sliding bars, each corresponding to a value mentioned above, that users can adjust until the colour of the glove is isolated from the rest of the colours. The link on line 10 needs to be changed every time the Wi-Fi network the camera is being used on changes and the program needs to be rerun every time the lighting/colour of the glove changes.



##### **Scoreboard Control**

&nbsp;	The third program, coded in C++, oversees the scoreboard, a buzzer and three buttons by interacting with the Arduino UNO. It reads the serial monitor and depending on what is sent through, it will add one to the Home or Guest Score, as seen from line 95 to line 107. It uses this information to keep track of when a set is over and sets a timer, that it displays, in between sets for three minutes.



**Figure 5.** 

*Steps the program takes to determine if a set has ended*
<img width="975" height="184" alt="image" src="https://github.com/user-attachments/assets/ac686f33-1819-458c-9793-52728c9fa9ab" />

&nbsp;

&nbsp;	It also uses this information to display the current period, as well as sets won for both Home and Guest sides. This program can initiate a timeout, when the left button is pressed, which delays the program for sixty seconds. This program also has access to an active buzzer that sounds before/after sets and before/after timeouts. The right button is also connected to this program, which is used during the first serve of a set. In addition to the right and left buttons, the program can also undo the last point given when the middle button is pressed. This program does not need to be rerun after running it once as the code will be stored in the Arduino.



##### **Main Python Program**

&nbsp;	The fourth program, coded in Python, brings the entire machine together and manages the image detecting/processing of the live stream while communicating with the third program. It uses the LH, LS, LV, UH, US, and UV values from the second program to isolate the colour of the glove from the live stream. It then finds the average coordinate of the colour of the glove and checks if it is between four pre-set ‘X’ values. If it is, it sees if it is between two pre-set ‘Y’ values. If the glove’s current position meets all the parameters, it means that the referee is signalling that a point was scored. The program has a thirteen-second delay after a point is scored to prevent it from detecting the referee’s clearance for service, which always follows a point, apart from at the beginning of the set. 



**Figure 6.** 

*Steps the program takes to determine if a point is scored*
<img width="644" height="870" alt="image" src="https://github.com/user-attachments/assets/872316fb-8906-4128-8782-6929be98fd93" />

&nbsp;

&nbsp;	By seeing which two of the four ‘X’ values the average coordinate of the colour was between, the program determines which side scored a point and tells the third program to add one to the corresponding side through the serial monitor. This program also stops for fifty-nine seconds when a timeout is called, one hundred seventy-nine seconds when a side wins a set and three seconds when the right button is pressed***1***. The link on line 13 needs to be changed every time the Wi-Fi network the camera is being used on changes. The LH, LS, LV, UH, US, and UV values on lines 16 and 17 need to be changed every time the lighting/colour of the glove changes. The parameters that a score is counted within, on lines 45 and 47, also need to be altered when the referee is replaced by another referee, or the machine is repositioned. This program needs to be rerun every time before the user uses the machine. 


***1***Refer to technical difficulties for the purpose of the right button





