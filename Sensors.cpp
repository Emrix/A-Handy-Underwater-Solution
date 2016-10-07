
// Big thanks to Nathan Day from Killpacks RAD lab : nathanday89@gmail.com 
// this program is the initial version for the new tactile sensor. 14 pins are powered while 6 pins are analog read pins

int Dpin[27]; 

char Apin[11] = {A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15};

void setup()
{
  Serial.begin(1000000);  
  
  //set and configure digital pins to outputs
 for( int i = 0; i < 11; i++)
 {
   pinMode(Apin[i],INPUT);
 }
   
  for( int i = 0; i < 13; i++) 
  {
   Dpin[i] = i+37;
   pinMode(Dpin[i],OUTPUT);
  }
  
   for( int i = 13; i < 27; i++) 
  {
   Dpin[i] = i+9;
   pinMode(Dpin[i],OUTPUT);
  }

}

void loop()
{
  // begin reading from row 1 column 1 and move through each column. Read from row 2 column 1 and read through each column...etc.
  for(int j = 0; j < 11; j++)
  {
    //print a row indicator to be used for keeping track of which rows are being read. 
    Serial.print(j);
    Serial.print('\t');
    
    // cycle through each of the digital I/O pins
    for(int i = 0; i < 27; i++)
    {
     digitalWrite(Dpin[i],HIGH);
     //delay(1);
     int val = analogRead(Apin[j]); 
     //delay(1);
     Serial.print(val);
     digitalWrite(Dpin[i],LOW);
     //delay(1);
     if(i < 26)
     {
       Serial.print("\t");
     }
     
    }
    
    Serial.println();
  }
}


/*
grid_sensor_code.txt
Open with
Displaying grid_sensor_code.txt.
*/
