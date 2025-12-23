### How this project was approached



\- Gather all the required materials

\- Connect the ESP-32 CAM to a computer

&nbsp; - The ESP-32 CAM was connected to an FTDI-Module, which was then be connected to a computer via a USB cable



\*\*Figure 3.\*\*



\_ESP-32 CAM Connected with an FTDI-Module\_ !\[A black wire with red and blue wires



\- Code a program to live stream the camera footage (C++)

&nbsp; - Modified code from How2Electronics

&nbsp; - Refer to \*\*ESP-32 CAM Setup\*\* in the \*\*Appendix\*\*

\- Code a program to find the LH, LS, LV, UH, US and UV values that isolates the chosen colour that is being detected on the live stream (Python)

&nbsp; - Used code from How2Electronics

&nbsp; - Refer to \*\*Colour Picker\*\* in the \*\*Appendix\*\*

\- Assemble scoreboard with a timeout button, an undo button and a first serve button

&nbsp; - Attach the prototype expansion board to the Arduino Uno

&nbsp; - Connect GND and 5V pins to a breadboard from the Arduino

&nbsp; - Connect all the individual pins for each display to the Arduino using the breadboard

&nbsp; - Connect the passive buzzer to the Arduino through the breadboard

&nbsp; - Connect buttons to Arduino using the smaller breadboard attached to the prototype expansion board

&nbsp; - Connect the small breadboard to the Arduino

&nbsp; - Connect the Arduino to a computer

&nbsp; - Design and print a scoreboard that has a spot for each display

&nbsp; - Tape displays onto the scoreboard



\*\*Figure 4.\*\*



\_The Scoreboard\_

\_Note\_: This image shows the scoreboard, that the third program controls, outside of its display case. Wires connect the displays, the buzzer, and the buttons to the Arduino, which has a cable that can be connected to a computer



\- Code a program to control the different displays on the scoreboard (Arduino IDE)-Refer to \*\*Scoreboard Control\*\* in the \*\*Appendix\*\*

&nbsp; - Use the TM1637Display, Ctype, SimpleTimer and SevSeg libraries

&nbsp; - Define the pins/variables

&nbsp; - Set up displays, buttons, and buzzer

&nbsp; - Have the program read the serial monitor

&nbsp; - Assign certain letters and numbers a command

&nbsp;   - Refer to lines 98-121 of \*\*Scoreboard Control\*\* in the \*\*Appendix\*\*

&nbsp;   - Add one to Home Score if 'X' is printed and print '1' on the serial monitor

&nbsp;   - Add one to Guest Score if 'Y' is printed and print '2' on the serial monitor

&nbsp;   - Add one to Sets Won (Home) if 'C' is printed and print '3' on the serial monitor

&nbsp;   - Add one to Sets Won (Guest) if 'V' is printed and print '4' on the serial monitor

&nbsp;   - Clear Home and Guest Scores if 'N' is printed

&nbsp; - Create a function that will keep track of the time between sets

&nbsp;   - Refer to lines 78-91 of \*\*Scoreboard Control\*\* in the \*\*Appendix\*\*

&nbsp;   - Print '5' onto the serial monitor

&nbsp;   - Set a variable to '0'

&nbsp;     - Create a count down from one hundred eighty seconds to indicate the time between a set

&nbsp;       - If the variable, defined at the beginning of the function as '0', is less than or equal to one hundred eighty, add one to the variable

&nbsp;       - Display the new variable on the timer display

&nbsp;       - Repeat until the variable is more than one hundred eighty

&nbsp;     - Sound the buzzer

&nbsp; - Have the program recognize when a set is over

&nbsp;   - Refer to lines 136-167 of \*\*Scoreboard Control\*\* in the \*\*Appendix\*\*

&nbsp;   - See if the Home Score or the Guest Score is more than 25 and the Home Score minus the Guest Score is equal to two or negative two

&nbsp;     - If so, the set is over

&nbsp;       - Add one to Sets Won (Home) if the Home Score minus the Guest Score is equal to two

&nbsp;       - Add one to Sets Won (Guest) if the Home Score minus the Guest Score is equal to negative two

&nbsp;       - Set the Home Score and the Guest Score to '0'

&nbsp;       - Sound the buzzer for half a second

&nbsp;       - Call the function in f. of step six

&nbsp; - Add a timeout button

&nbsp;   - Refer to lines 188-202 of \*\*Scoreboard Control\*\* in the \*\*Appendix\*\*

&nbsp;   - If the button is pressed:

&nbsp;     - Print '6' onto the serial monitor

&nbsp;     - Set a variable to '0'

&nbsp;     - Sound the buzzer

&nbsp;     - Have the program count down from sixty seconds to indicate the amount of time in a timeout

&nbsp;       - If the variable, defined at the beginning of h. as '0', is less than or equal to sixty, add one to the variable

&nbsp;       - Display the new variable on the timer display

&nbsp;       - Repeat until the variable is more than sixty

&nbsp;     - Sound the buzzer

&nbsp; - Add an undo button

&nbsp;   - Refer to lines 204-213 of \*\*Scoreboard Control\*\* in the \*\*Appendix\*\*

&nbsp;   - Record which side the last point was given to

&nbsp;   - If the button is pressed:

&nbsp;     - Subtract one from that side's point

&nbsp;     - Update the new score onto the displays

&nbsp; - Code the period display

&nbsp;   - Refer to lines 215-217 of \*\*Scoreboard Control\*\* in the \*\*Appendix\*\*

&nbsp;   - Add the Sets Won (Home) with the Sets Won (Guest) for the total amount of sets played

&nbsp;     - Add one to this equation to find the current period

&nbsp;   - Display the current period number onto the period display

&nbsp; - Detect when the game has ended

&nbsp;   - Refer to lines 170-186 of \*\*Scoreboard Control\*\* in the \*\*Appendix\*\*

&nbsp;   - Set a variable to equal either '3' or '5', depending on the number of sets that will be played

&nbsp;     - If the Sets Won for either Home or Guest equals to the variable, the game has ended

&nbsp;     - If this game has ended:

&nbsp;       - Sound buzzer

&nbsp;       - Delay for five minutes, which is enough time for the user to shut off the machine without any misfires)

\- Code a program that processes the live stream of the camera footage to determine what is happening in-game. This program should then be able to display this information on the scoreboard by communicating with the program in step six

&nbsp; - Use the cv2, Numpy, Time, Serial and Threading libraries

&nbsp; - Define a variable as nothing to use for loops

&nbsp; - Set up camera

&nbsp; - Connect to the serial monitor using the 'Serial' library

&nbsp; - Assign strings to the LH, LS, LV, UH, US, and UV values from step five

&nbsp; - Modify code found on How2Electronics to isolate the colour of the referee's glove from the rest of the colours

&nbsp;   - Find the coordinates of the center of the isolated colour

&nbsp; - Create a class that will recognize when points are scored and print bytes onto the serial monitor

&nbsp;   - Refer to lines 22-75 of the \*\*Main Python Code\*\* in the \*\*Appendix\*\*

&nbsp;   - Define variables 'last\_func' and 'betweensets' to equal to 'None'

&nbsp;   - Have a method, timeBetweenSets, that will delay the program from running during the break between sets

&nbsp;     - This method will call another method, delayBetweenSets, one hundred seventy-nine seconds after it has been called

&nbsp;     - It will set the variable 'betweensets' to 1

&nbsp;   - Have a method, TenSecondDelay, that will set the 'last\_func' to 'None'

&nbsp;   - Have a method, delayBetweenSets, that will set 'betweensets' to '1' and print 'N' onto the serial monitor

&nbsp;   - Have a method, detectColourPos, that will determine if a point is scored or not

&nbsp;     - First, it will see if 'betweensets' is equal to '1'

&nbsp;       - If it is not, it will see if the coordinate from f. (step 7) is between certain boundaries on the right and left sides of the live stream



If it is within a certain set of coordinates on the left side, it will call the method 'connectionToArduinoX' (defined below)



If it is within a certain set of coordinates on the right side, it will call the method 'connectionToArduinoY' (defined below)



\- - - Have a method, connectionToArduinoX, that will give a point to 'Home'

&nbsp;           - Firstly, it will see if 'last\_func' is equal to 'connectionToArduinoX'

&nbsp;               - \*\*\_This will prevent the method from giving more than one point to home\_\*\*

&nbsp;               - If it is not:



Print 'X' onto the serial monitor



Call the method 'ThirteenSecondDelay' in thirteen seconds



Set 'last\_func' to equal 'connectionToArduinoX'



\- - - Have a method, connectionToArduinoY, that will give a point to 'Guest'

&nbsp;           - Firstly, it will see if 'last\_func' is equal to 'connectionToArduinoY'

&nbsp;               - \*\*\_This will prevent the method from giving more than one point to guest\_\*\*

&nbsp;               - If it is not:



Print 'Y' onto the serial monitor



Call the method 'ThirteenSecondDelay' in thirteen seconds



Set 'last\_func' to equal 'connectionToArduinoY'



\- 1. Create a function that reads the Serial Monitor

&nbsp;       - Refer to lines 81-88 of the \*\*Main Python Code\*\* in the \*\*Appendix\*\*

&nbsp;       - If a '5' is printed, call 'timeBetweenSets' from g. (step 7)

&nbsp;       - If a '6' is printed, delay the program for fifty-nine seconds

&nbsp;       - If a '9' is printed, delay the program for three seconds

