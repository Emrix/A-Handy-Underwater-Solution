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

class HUS:
        # Start the serial connection with the Arduino over specified ports
        # This baud rate should match up with the Arduino's set baud rate.
        # This is the USB port that the arduino is connected to.  If you don't know what
        # the port is, open the Arduino program, and check to see what serial port the Arduino
        # is connected to.
        def __init__(self, port, baudrate):
                # This is simply a variable that will tell us if the Arduino is connected or not
                self.arduinoConnected = False
                # the Object that contains the serial interface, we initialize it here with nothing
                self.ser = serial.Serial(port, baudrate)
                # loop until the arduino says it's ready
                while not self.arduinoConnected:
                        serin = self.ser.read() # Wait until we receive data (possible timeout?)
                        self.arduinoConnected = True

        # Close the open port
        def stop(self):
                self.ser.close()
                self.arduinoConnected = False

        def move(self, servoNum, location):
                if self.arduinoConnected == False:
                        return 0
                # Data validation
                if servoNum > 16:
                        servoNum = 16
                if servoNum < 1:
                        servoNum = 1
                if location > 255:
                        location = 255
                if location < 1:
                        location = 1
                # Send the Data
                self.ser.write(chr(servoNum))
                self.ser.write(chr(location))
                # Read the result (the potentiometer output)
                position = self.ser.read()
                return ord(position)
