import serial
import time
import pyautogui
ser = serial.Serial('/dev/ttyACM1')
ser.baudrate = 9600
ser.close()
print ('Using SerialPort:')
print (ser.name)

ser.open()
while True:
	
	x = float(ser.readline().strip())		
	time.sleep(0.001)

	y = float(ser.readline().strip())
	time.sleep(0.001)
	if(x == 547 or y == 547):
		pyautogui.click()
		x = 50
		y = 50
	if(x == 896 or y == 896):
		pyautogui.click(button='right')
		x = 50
		y = 50

	x = x-50
	y = (y-50)*-1
	if(x == 1 or x == -1):
		x = 0

	if(y == 1 or y == -1):
		y = 0		

	a = str(x)
	b = str(y)		
	print("X = " + a)
	print("Y = " + b)
	
	width, height = pyautogui.size()
	pyautogui.PAUSE = 0
	pyautogui.FAILSAFE = False
	pyautogui.moveRel(x, y, duration = 0)

	

	
