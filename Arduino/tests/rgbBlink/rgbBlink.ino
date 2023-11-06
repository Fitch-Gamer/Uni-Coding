int RPin = 5;
int GPin = 6;
int BPin = 7;
int i = 0;
void setup(){
  // put your setup code here, to run once:
  pinMode(RPin, OUTPUT);
  pinMode(GPin, OUTPUT);
  pinMode(BPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  switch (i%3)
  {
    case 0:
      digitalWrite(RPin, HIGH);
      digitalWrite(GPin, LOW);
      digitalWrite(BPin, LOW);
      break;

    case 1:
      digitalWrite(RPin, LOW);
      digitalWrite(GPin, HIGH);
      digitalWrite(BPin, LOW);
      break;

    case 2:
      digitalWrite(RPin, LOW);
      digitalWrite(GPin, LOW);
      digitalWrite(BPin, HIGH);
      break;
  }

  i++;
  delay(500);
}
