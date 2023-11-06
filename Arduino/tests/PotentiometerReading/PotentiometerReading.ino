#include <Servo.h>
Servo servo1;
int servoPin = 9;
int potpin = A0;
int val;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo1.attach(servoPin);
}

void loop() {
  // put your main code here, to run repeatedly:
  val = analogRead(potpin);
  
  val = val;
  val = map(val, 0, 1023, 0, 180);
  Serial.println(val);
  servo1.write(val);
  delay(1);
}
