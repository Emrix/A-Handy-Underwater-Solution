int incomingByte = 0;   // for incoming serial data
char byteChar;

void setup() {
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
        Serial.write('1');
}

void loop() {
        // send data only when you receive data:
        if (Serial.available() > 0) { //If there is data present
                // read the incoming byte:
                incomingByte = Serial.read();
                byteChar = incomingByte;

                // say what you got:
                Serial.write(byteChar);
                //Serial.print(byteChar);
        }
}
