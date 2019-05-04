# MouseChuck
Arduino+python pyautogui to control cursor with a Wii nunchuk

Code is divided in two main parts : Arduino code and python code.
The arduino code uses the library nunchuk.h (I added only some function at the end of file), you can modify some calibration parameters depending on your nunchuk, this is the link to the library for more info: https://github.com/infusion/Fritzing/tree/master/Nunchuk (Copyright (c) 2016, Robert Eisele (robert@xarg.org)
Dual licensed under the MIT or GPL Version 2 licenses).
The python code uses the library pyautogui to move the cursor using the values arduino passes through serial: https://pyautogui.readthedocs.io/en/latest/ 


The use and setup is simple: connect the nunchuk to arduino through jumper cables, you need 4 different cabled to connect 3.3v, gnd, data1 and data2. 
Load the code into arduino, and run the python script using python3 from cli.
In line 4 of file MouseChuk.py you can modify the serial port depending on wich you are using.
At the first run python may encounters a problem, like:
File "MouseChuck.py", line 16, in <module>
    x = float(ser.readline().strip())		
ValueError: could not convert string to float:
. 
 
Just run the code again (and again if necessary), it will work.
So, now you can use the nunchuk as a mouse, the joystick control the cursor, C burtton is the left click, Z, the right.
I had to implement the scrolling using the nunchuk accelerometer, and fix lot of bugs, like the previous I described.
This cod works perfectly on my machine, a desktop computer running Arch Linux, but I'm pretty sure will work even on other Linux, Windows, and MacOS machines, it will work on every screen size, !Does not work well on multi-monitor systems!
It's not tested for games, but it will be the best final usage, so try it.

So you need:
-Ardunio uno.
-4 jumper wires
-Wii nunchuk
-python3 installed
-python pyautogui library installed
-python serial library installed

This is a totally experimental project, there are lot of things to fix or adjust, so use it and work on it to fix your needs.
The operation is pretty simple: Arudino read values from nunchuk sensors, calculates the x and y movements with some math, and sends values through Serial, the Python3 code read the values from serial, does some math, and uses pyautogui to move the cursor.


  
  
  


