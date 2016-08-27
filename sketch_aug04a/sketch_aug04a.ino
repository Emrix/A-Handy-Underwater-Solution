/***************************************************
 * The Arduino uses I2C to communicate with the servo driver; 2 pins are required to
 * interface. For Arduino UNOs, thats SCL -> Analog 5, SDA -> Analog 4
 * The Arduino also uses the USB to interface with external programs over serial.
 * All the potentiometer inputs on the arduino MUST correspond to the servo outputs on the I2C board
 ****************************************************/

//Include our libraries here
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
//This determines what the baud rate is for the serial connection.
//This should be the same in the arduino as the python program, or it wont work.
#define BAUD_RATE 9600
//This defines how many servos we are using in our system.
#define NUMBER_OF_SERVOS 9
//This is the 'minimum' pulse length count (out of 4096)
#define SERVOMIN 150
//This is the 'maximum' pulse length count (out of 4096)
#define SERVOMAX 600
//Each new board is called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
//The following array keeps track of the current Pulse Length of all the servos
double pulseLen[NUMBER_OF_SERVOS];
//incomingByte comes from the serial connection, and it determines what servo is moved
//and what way it moves.
uint8_t incomingByte;
//We set this var so know what direction the servo is moving
bool goingForward;

void setup() {
  //Set default values for all servos (350 should be about midpoint for most servos)
  for (int x = 0; x < NUMBER_OF_SERVOS; x++) {
    pulseLen[x] = 350;
  }
  Serial.begin(BAUD_RATE);
  pwm.begin();
  pwm.setPWMFreq(60); // Analog servos run at ~60 Hz updates
}

//Retrieve A Bit (servoCommand) from Serial Port (ie: 001, 060, 061, 121, 140, 161)
//The first two digits represent the servo number, and the last digit represents
//a forward or backward motion.  That way we can keep everything within an uint8_t.
//Then we send the built in potentiometer output for the motor back through the serial port.
void loop() {
  if (Serial.available() > 0) { //if it's not available, than we shouldn't do anything

    //Read Incoming byte
    incomingByte = Serial.read(); /*There may be a timeout for the serial.read, so we may need to handle that*/

    //If there is a 1 on the end of it, the servo moves forward, if it's a 0, it moves backward
    //servoCommand divided by 10 (integer division) results in the servo we want to control
    goingForward = incomingByte % 2;
    incomingByte = incomingByte / 10;

    //This is just something to say that there was no servo that we were told to move
    if (incomingByte < NUMBER_OF_SERVOS) {
      Serial.println(0);
    } 
    else {

      //Update the database right here to what our current position should be
      if (goingForward) {
        pulseLen[incomingByte] = pulseLen[incomingByte] + 1;
      } 
      else {
        pulseLen[incomingByte] = pulseLen[incomingByte] - 1;
      }

      //Do some data validation here, make sure we aren't going to break anything.
      if (pulseLen[incomingByte] < SERVOMIN) {
        pulseLen[incomingByte] = SERVOMIN;
      } 
      else if (pulseLen[incomingByte] > SERVOMAX) {
        pulseLen[incomingByte] = SERVOMAX;
      }

      //Actually move the servo forward or backward by 1 pulse length(?)
      pwm.setPWM(incomingByte, 0, pulseLen[incomingByte]);

      //Send back the potentiometer output through the serial port
      Serial.println(analogRead(incomingByte));
    }
  }
}




