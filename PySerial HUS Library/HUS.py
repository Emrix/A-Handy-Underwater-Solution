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
	'''Add In: Check to see if a port is already open, and if there is then close it'''
	# Open the serial port
	ser = serial.Serial(port, baudRate)
	'''Add In: check to see if it actually opened'''
	# loop until the arduino says it's ready
	while not arduinoConnected:
	    serin = ser.read()
	    arduinoConnected = True
	    '''Add In: have a time out feature if it doesn't connect'''
	return True

# Close the open port
def stop()
	ser.close()

# How to write data to the serial port if it's open
def write(data)
	'''Add In: check to see if there is an open port or not'''
	ser.write(data)
	'''Add In: check to see if it received the info or not'''
	return True

def read()
	'''Add In: check to see if there is an open port or not'''
	data = ser.read()
	return data

def move(servoNum,forward)
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
		revertMove = moveData
		moveData = moveData + 1
	else:
		revertMove = moveData + 1
	positionData = servoNum + 200
	# Get previous servo position
	write(positionData)
	previousPosition = ser.read()
	# Move the Servo
	write(moveData)
	# Check to see if it actually moved
	write(positionData)
	currentPosition = ser.read()
	if currentPosition == previousPosition:
		#The move failed, and we should punish the algorithm
		write(revertMove)
		return False
	else
		return True





'''
servoNum*10 + 1/0 for servo being moved forward or backward (max = 151)
Anything above 200 would be referring to some sort of potentiometer pin.
the touch pin would not be connected on this arduino
'''