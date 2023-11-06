int LedPin = 8;
void setup() {
  // put your setup code here, to run once:
  pinMode(LedPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LedPin, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LedPin, LOW);   // turn the LED off by making the voltage LOW
  delay(1000); 

}
