/***************************************************
   The Arduino uses I2C to communicate with the servo driver; 2 pins are required to
   interface. For Arduino UNOs, thats SCL -> Analog 5, SDA -> Analog 4
   The Arduino also uses the USB to interface with external programs over serial.
   All the potentiometer inputs on the arduino MUST correspond to the servo outputs on the I2C board
 ****************************************************/

//Include our libraries here
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
//This determines what the baud rate is for the serial connection.
//This should be the same in the arduino as the python program, or it wont work.
#define BAUD_RATE 9600
//This defines how many servos we are using in our system.
#define NUMBER_OF_SERVOS 16
//This is the 'minimum' pulse length count (out of 4096)
#define SERVOMIN 150
//This is the 'maximum' pulse length count (out of 4096)
#define SERVOMAX 600
//Each new board is called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
//incomingByte is data from the serial connection, and it determines the servo
//number, as well as the position it is moved to
int incomingByte;
int servo;
int pos;
//The returning data
char byteChar;

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
  //Set default values for all servos (350 should be about midpoint for most servos)
  Serial.begin(BAUD_RATE);
  Serial.write('1');
  pwm.begin();
  pwm.setPWMFreq(60); // Analog servos run at ~60 Hz updates
  for (int x = 0; x < NUMBER_OF_SERVOS; x++) {
    delay(500);
    pwm.setPWM(x, 0, 350);
  }
}

//Retrieve a bit (servo) from Serial Port (ie: 1, 2, 5, 9, 16)
//Retrieve another bit (position) from Serial Port (ie: 150, 243, 501, 600)
//We move the servo to the specified position, and then
//Then we send the built in potentiometer output for the motor back through the serial port.
void loop() {
  if (Serial.available() > 0) { //if if there is data present
    //Read Incoming byte
    incomingByte = Serial.read();
    //transform the byte into an int
    servo = incomingByte;
    servo--;
    //repeat for the position
    incomingByte = Serial.read();
    pos = incomingByte;
    pos--;

    //This is just something to say that there was no servo that we were told to move
    if (servo >= NUMBER_OF_SERVOS) {
      Serial.write('N'); //N is for number of servos error
    } else if (servo == 256) {
      Serial.write('T'); //T is for a potential timeout error
    } else {
      //We have to do some formatting with the position data to map it correctly
      pos = ((SERVOMAX-SERVOMIN)/255*pos);
      //Do some data validation here, make sure we aren't going to break anything.
      if (pos < SERVOMIN) {
        pos = SERVOMIN;
      }
      else if (pos > SERVOMAX) {
        pos = SERVOMAX;
      }

      //Actually move the servo to the specified pulse length
      pwm.setPWM(servo, 0, pos);

      //Send back the potentiometer output through the serial port
      byteChar = analogRead(servo);
      Serial.write(byteChar);
    }
    incomingByte = 256;
  }
}
