int RPin = 9;
int GPin = 5;
int BPin = 6;
int potpin = A0;
int PotVal = 0;
int ButPin = 13;
bool ButSwitch = false;
void setup(){
  // put your setup code here, to run once:
  pinMode(RPin, OUTPUT);
  pinMode(GPin, OUTPUT);
  pinMode(BPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  ButSwitch = digitalRead(ButPin)==1;
  Serial.println(digitalRead(ButPin));
  if(ButSwitch)
  {
    PotVal = analogRead(potpin);
    PotVal = map(PotVal, 0, 1023, 0, 768);
    if(PotVal<256) 
    {
      analogWrite(RPin, 255);
      analogWrite(GPin, PotVal);
      analogWrite(BPin, 255-PotVal);

    }
    else if(PotVal<512)
    {
      int x = PotVal-256;
      analogWrite(RPin, 255-x);
      analogWrite(GPin, 255);
      analogWrite(BPin, x);
    }
    else
    {
      int x = PotVal-512;
      analogWrite(RPin, x);
      analogWrite(GPin, 255-x);
      analogWrite(BPin, 255);
    }
  }
  delay(10);
}
