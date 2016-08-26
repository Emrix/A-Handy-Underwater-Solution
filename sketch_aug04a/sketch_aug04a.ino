/***************************************************
  These displays use I2C to communicate, 2 pins are required to
  interface. For Arduino UNOs, thats SCL -> Analog 5, SDA -> Analog 4
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// eacy new board is called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
//More can be called with a different addresses
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);

#define NUMBER_OF_SERVOS = 0 //this is how many servos we actually have connected to the board

//this determines what the baud rate is for the serial connection.
//This should be the same in the arduino as the python program, or it wont work.
#define BAUD_RATE = 9600

uint8_t incomingByte = 0;
bool goingForward;
int potentiometerPin;

void setup() {
  Serial.begin(BAUD_RATE);
  pwm.begin();
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates
  yield();
}

void loop() {
  //Retrieve A Bit (servoCommand) from Serial Port (eg 001, 060, 061, 121, 140, 161)
  //The first two digits represent the servo number, and the last digit represents
  //a forward or backward motion.  That way we can keep everything within an uint8_t.
  if (Serial.available() > 0) { //if it's not available, than we shouldn't do anything
    //Read Incoming byte
    incomingByte = Serial.read();
    //There may be a timeout for the serial.read, so we'll have to handle that here
    if (incomingByte != 0) {

      //if servoCommand mod 2 is one than the servo moves forward, else it moves backward
      //servoCommand divided by 10 (integer division) results in the servo we want to control
      goingForward = incomingByte % 2;
      //1 It's going forward
      //0 It's going backward
      incomingByte = incomingByte / 10;

      //capture the current potentiometer output for that servo
      //attempt to move the servo forward or backward by 1
      //capture the current potentiometer output again
      //All the potentiometer inputs on the arduino MUST correspond to the servo outputs on the I2C board
      potentiometerPin = analogRead(incomingByte);
      if (goingForward) {
        pwm.setPWM(incomingByte, 0, pulselen+1); //Double Check this, we may need to keep the state of all servos
      } else {
        pwm.setPWM(incomingByte, 0, pulselen-1); //Double Check this, we may need to keep the state of all servos
      }
      
      //if the potentiometer outputs are the same, than send back a fail message
      //if the potentiometer outputs are different (depending on the desired outcome) send back a success message
      //move the servo to it's original position (to avoid stalling)
      delay(100); //This may or may not be needed to allow the servo to actually move
      if (potentiometerPin = analogRead(incomingByte)) {
        //The Motor didn't actually move, so we put it back just to make sure it's protected
        pwm.setPWM(incomingByte, 0, pulselen); //Double Check this, we may need to keep the state of all servos
        Serial.println(0); //Failure
      } else {
        //The Servo did move, so we keep it where it was, and update the value
        pulselen = (pulselen * 2 - 1);
        Serial.println(1); //Success
      }
    }
  }
  //Reset the incomingByte
  incomingByte = 0;
}
