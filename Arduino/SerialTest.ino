#include<Wire.h>
void setup() {
pinMode(13,OUTPUT);
Serial.begin(9600); // set the baud rate
Serial.println("Ready"); // print "Ready" once
}
void loop() {
if(Serial.available()> 0){ // only send data back if data has been sent
if(Serial.read()=='s')
{
  
  digitalWrite(13,HIGH);
  delay(10000);
}
else{
  digitalWrite(13,LOW);
}
}
 // delay for 1/10 of a second
}
