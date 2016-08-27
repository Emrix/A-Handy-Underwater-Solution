'''
A Handy Underwanter Solution (HUS) Arduino Serial Communication Library

Created on 2016-8-25

@author: Matt Ricks

To use this code as a library, move this file near where your main code files is
and then use "import HUS.py".  Once you've done that, you can simply use HUS.move()
to control the servos from the arduino.
'''

# Serial Library, the key to this whole thing.
import serial

# This is simply a variable that will tell us if the Arduino is connected or not
arduinoConnected = False

# the Object that contains the serial interface, we initialize it here with nothing
ser = serial.Serial("", "")

# Start the serial connection with the Arduino over specified ports
# This baud rate should match up with the Arduino's set baud rate.
# This is the USB port that the arduino is connected to.  If you don't know what
# the port is, open the Arduino program, and check to see what serial port the Arduino
# is connected to.
def start(port,baudRate)
	# Close the port just to make sure
	ser.close()
	# Open the serial port
	ser = serial.Serial(port, baudRate)
	# loop until the arduino says it's ready
	while not arduinoConnected:
	    serin = ser.read() # Wait until we receive data (possible timeout?)
	    arduinoConnected = True
	    '''Add In: have a more advanced time out feature if it doesn't connect'''
	return True

# Close the open port
def stop()
	ser.close()
	arduinoConnected = False

def move(servoNum,forward)
	if arduinoConnected == False:
		return 0
	# Data validation
	if servoNum > 15:
		servoNum = 15
	if servoNum < 0:
		servoNum = 0
	if forward != True:
		forward = False
	# Formatting data
	moveData = servoNum * 10
	if forward:
		moveData = moveData + 1
	# Move the Servo
	ser.write(data)
	# Read the result (the potentiometer output)
	position = ser.read()
	return position