#Mousechuk.py Antonio Del Cogliano 12/05/2019
#Fixed bugs, added scroll with nunchuk's acellerometer
import serial
import time
import pyautogui
ser = serial.Serial('/dev/ttyACM0')
ser.baudrate = 9600
speed = 10 #this value is the speed (like dpi) for the cursor movement
'''speed became 0 in the process so, at y and x value 10 the cursor will not move'''
scrollSpeed = 5
auto_rerun = True #auto_rerun can retry to ecxecute the code if something goes wrong
print ('Using SerialPort:')
print (ser.name)


def main(): #the main function
	'''serial port can output wrong values (not numbers) 
	so the try-except rerun the code if something goes wrong'''
	try:
		ser.close()
		print('Trying to connect device at '+(ser.name))
		ser.open()	   
		while True: #loop the function
				
			x = float(ser.readline().strip()) #the first readed value is the x axis value		
			time.sleep(0.001)#wait for 1 millisecond          	

			y = float(ser.readline().strip()) #the second is the y axis value
			time.sleep(0.001)
			while(x == 547 or y == 547): #this value (547) is the left click input
				pyautogui.click(clicks=1)
				x = speed #don't move the cursor (cannot move the cursor if you're clicking)
				y = speed
			while(x == 896 or y == 896): #this value (896) is the right click input
				pyautogui.click(button='right')
				x = speed
				y = speed
			while(x == 354 or y == 354): #this value (354) is the up scroll inpuyt
				pyautogui.scroll(scrollSpeed)
				x = speed #don't move the cursor (cannot move the cursor if you're scrolling)
				y = speed	
			while(x == 657 or y == 657): #this value (657) is the down scroll input
				pyautogui.scroll(-scrollSpeed)
				x = speed #don't move the cursor (cannot move the cursor if you're scrolling)
				y = speed	
			'''some math to adjust the x and y values'''	
			x = x-speed
			y = (y-speed)*-1
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
			pyautogui.moveRel(x, y, duration = 0) #move the cursor relatively to his current position by x and y values
	except:
		if (auto_rerun == True):
			print('An error occurred, rerun: on, rerunning code...')
			main() #re-run the main()function
		else:
			print('An error occurred, rerun: off, closing...')	
				
					
main()
	

	
