# <a name="_toc95170653"></a>How this project was approached 
1. Gather all the required materials 
1. Connect the ESP-32 CAM to a computer 
   1. The ESP-32 CAM was connected to an FTDI-Module, which was then be connected to a computer via a USB cable 

**Figure 3.**

*ESP-32 CAM Connected with an FTDI-Module*
<img width="786" height="443" alt="image" src="https://github.com/user-attachments/assets/34ca01d6-f963-44c0-ab92-77473cdfa507" />


1. Code a program to live stream the camera footage (C++)
   1. Modified code from How2Electronics
   1. Refer to **ESP-32 CAM Setup** in the **Appendix**
1. Code a program to find the LH, LS, LV, UH, US and UV values that isolates the chosen colour that is being detected on the live stream (Python)
   1. Used code from How2Electronics
   1. Refer to **Colour Picker** in the **Appendix**
1. Assemble scoreboard with a timeout button, an undo button and a first serve button
   1. Attach the prototype expansion board to the Arduino Uno
   1. Connect GND and 5V pins to a breadboard from the Arduino 
   1. Connect all the individual pins for each display to the Arduino using the breadboard
   1. Connect the passive buzzer to the Arduino through the breadboard
   1. Connect buttons to Arduino using the smaller breadboard attached to the prototype expansion board
   1. Connect the small breadboard to the Arduino 
   1. Connect the Arduino to a computer
   1. Design and print a scoreboard that has a spot for each display
   1. Tape displays onto the scoreboard

**Figure 4.**

*The Scoreboard*
<img width="504" height="672" alt="image" src="https://github.com/user-attachments/assets/a2e0d11a-e6f4-42bb-9b40-6d56eed7818e" />
*Note*: This image shows the scoreboard, that the third program controls, outside of its display case. Wires connect the displays, the buzzer, and the buttons to the Arduino, which has a cable that can be connected to a computer

1. Code a program to control the different displays on the scoreboard (Arduino IDE)—Refer to **Scoreboard Control** in the **Appendix** 
   1. Use the TM1637Display, Ctype, SimpleTimer and SevSeg libraries 
   1. Define the pins/variables
   1. Set up displays, buttons, and buzzer
   1. Have the program read the serial monitor
   1. Assign certain letters and numbers a command
      1. Refer to lines 98-121 of **Scoreboard Control** in the **Appendix**
      1. Add one to Home Score if ‘X’ is printed and print ‘1’ on the serial monitor
      1. Add one to Guest Score if ‘Y’ is printed and print ‘2’ on the serial monitor
      1. Add one to Sets Won (Home) if ‘C’ is printed and print ‘3’ on the serial monitor
      1. Add one to Sets Won (Guest) if ‘V’ is printed and print ‘4’ on the serial monitor
      1. Clear Home and Guest Scores if ‘N’ is printed
   1. Create a function that will keep track of the time between sets
      1. Refer to lines 78-91 of **Scoreboard Control** in the **Appendix**
      1. Print ‘5’ onto the serial monitor 
      1. Set a variable to ‘0’
         1. Create a count down from one hundred eighty seconds to indicate the time between a set
            1. If the variable, defined at the beginning of the function as ‘0’, is less than or equal to one hundred eighty, add one to the variable
            1. Display the new variable on the timer display
            1. Repeat until the variable is more than one hundred eighty
         1. Sound the buzzer 
   1. Have the program recognize when a set is over
      1. Refer to lines 136-167 of **Scoreboard Control** in the **Appendix**
      1. See if the Home Score or the Guest Score is more than 25 and the Home Score minus the Guest Score is equal to two or negative two
         1. If so, the set is over	
            1. Add one to Sets Won (Home) if the Home Score minus the Guest Score is equal to two 
            1. Add one to Sets Won (Guest) if the Home Score minus the Guest Score is equal to negative two
            1. Set the Home Score and the Guest Score to ‘0’
            1. Sound the buzzer for half a second 
            1. Call the function in f. of step six
   1. Add a timeout button
      1. Refer to lines 188-202 of **Scoreboard Control** in the **Appendix**
      1. If the button is pressed:
         1. Print ‘6’ onto the serial monitor 
         1. Set a variable to ‘0’
         1. Sound the buzzer
         1. Have the program count down from sixty seconds to indicate the amount of time in a timeout
            1. If the variable, defined at the beginning of h. as ‘0’, is less than or equal to sixty, add one to the variable
            1. Display the new variable on the timer display
            1. Repeat until the variable is more than sixty
         1. Sound the buzzer 
   1. Add an undo button
      1. Refer to lines 204-213 of **Scoreboard Control** in the **Appendix**
      1. Record which side the last point was given to
      1. If the button is pressed:
         1. Subtract one from that side’s point
         1. Update the new score onto the displays 
   1. Code the period display
      1. Refer to lines 215-217 of **Scoreboard Control** in the **Appendix**
      1. Add the Sets Won (Home) with the Sets Won (Guest) for the total amount of sets played
         1. Add one to this equation to find the current period
      1. Display the current period number onto the period display
   1. Detect when the game has ended
      1. Refer to lines 170-186 of **Scoreboard Control** in the **Appendix**
      1. Set a variable to equal either ‘3’ or ‘5’, depending on the number of sets that will be played
         1. If the Sets Won for either Home or Guest equals to the variable, the game has ended
         1. If this game has ended:
            1. Sound buzzer
            1. Delay for five minutes, which is enough time for the user to shut off the machine without any misfires)
1. Code a program that processes the live stream of the camera footage to determine what is happening in-game. This program should then be able to display this information on the scoreboard by communicating with the program in step six
   1. Use the cv2, Numpy, Time, Serial and Threading libraries 
   1. Define a variable as nothing to use for loops
   1. Set up camera 
   1. Connect to the serial monitor using the ‘Serial’ library 
   1. Assign strings to the LH, LS, LV, UH, US, and UV values from step five
   1. Modify code found on How2Electronics to isolate the colour of the referee’s glove from the rest of the colours 
      1. ` `Find the coordinates of the center of the isolated colour 
   1. Create a class that will recognize when points are scored and print bytes onto the serial monitor 
      1. Refer to lines 22-75 of the **Main Python Code** in the **Appendix**
      1. Define variables ‘last\_func’ and ‘betweensets’ to equal to ‘None’
      1. Have a method, timeBetweenSets, that will delay the program from running during the break between sets
         1. This method will call another method, delayBetweenSets, one hundred seventy-nine seconds after it has been called
         1. It will set the variable ‘betweensets’ to 1
      1. Have a method, TenSecondDelay, that will set the ‘last\_func’ to ‘None’
      1. Have a method, delayBetweenSets, that will set ‘betweensets’ to ‘1’ and print ‘N’ onto the serial monitor
      1. Have a method, detectColourPos, that will determine if a point is scored or not 
         1. First, it will see if ‘betweensets’ is equal to ‘1’
            1. If it is not, it will see if the coordinate from f. (step 7) is between certain boundaries on the right and left sides of the live stream
               1. If it is within a certain set of coordinates on the left side, it will call the method ‘connectionToArduinoX’ (defined below)
               1. If it is within a certain set of coordinates on the right side, it will call the method ‘connectionToArduinoY’ (defined below)
      1. Have a method, connectionToArduinoX, that will give a point to ‘Home’
         1. Firstly, it will see if ‘last\_func’ is equal to ‘connectionToArduinoX’
            1. ***This will prevent the method from giving more than one point to home***
            1. If it is not: 
               1. Print ‘X’ onto the serial monitor
               1. Call the method ‘ThirteenSecondDelay’ in thirteen seconds
               1. Set ‘last\_func’ to equal ‘connectionToArduinoX’
      1. Have a method, connectionToArduinoY, that will give a point to ‘Guest’
         1. Firstly, it will see if ‘last\_func’ is equal to ‘connectionToArduinoY’
            1. ***This will prevent the method from giving more than one point to guest***
            1. If it is not: 
               1. Print ‘Y’ onto the serial monitor
               1. Call the method ‘ThirteenSecondDelay’ in thirteen seconds
               1. Set ‘last\_func’ to equal ‘connectionToArduinoY’
   1. Create a function that reads the Serial Monitor
      1. Refer to lines 81-88 of the **Main Python Code** in the **Appendix**
      1. If a ‘5’ is printed, call ‘timeBetweenSets’ from g. (step 7)
      1. If a ‘6’ is printed, delay the program for fifty-nine seconds
      1. If a ‘9’ is printed, delay the program for three seconds


