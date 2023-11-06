#include <Servo.h>

Servo servo1;

int const NumLights = 3;

int const P1LightStartPin = 2;
int const P1ButPin = 5;

int const P2LightStartPin = 8;
int const P2ButPin = 11;

int const ScorePin = 13;

const int ServoPin = 6;

int MaxTime = 1000;

int P1CurrTime = 0;
int P2CurrTime = 0;

int P1CurrLightOn = -1;
int P2CurrLightOn = -1;

int P1Score = 0;
int P2Score = 0;

int MaxScore = 10;

int MinDelay = 200;
int MaxDelay = 1500;
int ScoreDelay = 50;

int P1WaitDelay = 0;
int P2WaitDelay = 0;

const int LatchPin = 7
const int DataPin

//int LightPins[NumLights];
//int ButPins[NumLights];


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  InitAll(P1LightStartPin, P1LightStartPin+NumLights-1,OUTPUT);
  InitAll(P2LightStartPin, P2LightStartPin+NumLights-1,OUTPUT);

  pinMode(P1ButPin, INPUT);
  pinMode(P2ButPin, INPUT);

  pinMode(ScorePin, OUTPUT);

  servo1.attach(ServoPin);
}

void loop() {
  // put your main code here, to run repeatedly:
  servo1.write(90+((90/MaxScore)*(P2Score-P1Score)));
  
  if (P1CurrTime>=MaxTime && P1WaitDelay<=0)
  {
    P1CurrTime=0;
    AllLow(P1LightStartPin, P1LightStartPin+NumLights-1);
    int RandomNum = rand() % NumLights;
    P1CurrLightOn = RandomNum;
    digitalWrite((RandomNum+P1LightStartPin), HIGH);
  }

  if(digitalRead(P1ButPin)==HIGH && P1WaitDelay <= 0)
  {
    P1ScorePoint(1);
    P1CurrTime=MaxTime;
    AllLow(P1LightStartPin, P1LightStartPin+NumLights-1);
    Serial.println(P1Score);
    P1WaitDelay = rand()%(MaxDelay-MinDelay) + MinDelay;
  }


  if (P2CurrTime>=MaxTime && P2WaitDelay<=0)
  {
    P2CurrTime=0;
    AllLow(P2LightStartPin, P2LightStartPin+NumLights-1);
    int RandomNum = rand() % NumLights;
    P1CurrLightOn = RandomNum;
    digitalWrite((RandomNum+P2LightStartPin), HIGH);
  }

  if(digitalRead(P2ButPin)==HIGH && P2WaitDelay<=0)
  {
    P2ScorePoint(1);
    P2CurrTime=MaxTime;
    AllLow(P2LightStartPin, P2LightStartPin+NumLights-1);
    Serial.println(P2Score);
    P2WaitDelay = rand()%(MaxDelay-MinDelay) + MinDelay;
  }

  P1CurrTime++;
  P2CurrTime++;

  P1WaitDelay--;
  P2WaitDelay--;
  delay(1);
}

void(* resetFunc) (void) = 0;

void AllLow(int start, int end)
{
  for(int i=start;i<=end;i++)
  {
    digitalWrite(i, LOW);
  }
}

void InitAll(int start, int end, int type)//int[] InitAll(int start, int end, int type)
{
  //int OutPut[end-start+1];
  //int j = 0;
  for(int i=start;i<=end;i++)
  {
    pinMode(i, type);
    //OutPut[j] = i;
    //j++;
  }
}
void P1ScorePoint(int points)
{
  P1Score += points;
  digitalWrite((ScorePin), HIGH);
  delay(ScoreDelay);
  digitalWrite((ScorePin), LOW);
  if (P1Score>=MaxScore)
  {
    P1Win();
  }
}
void P2ScorePoint(int points)
{
  P2Score += points;
  digitalWrite((ScorePin), HIGH);
  delay(ScoreDelay);
  digitalWrite((ScorePin), LOW);
  if (P2Score>=MaxScore)
  {
    P2Win();
  }

}

void P2Win()
{
  AllLow(P1LightStartPin, P1LightStartPin+NumLights-1);
  AllLow(P2LightStartPin, P2LightStartPin+NumLights-1);
  for(int i = 0;i<5; i++)
  {
    for(int i=P2LightStartPin;i<=P2LightStartPin+NumLights-1;i++)
    {
      digitalWrite(i, HIGH);
    }
    digitalWrite(ScorePin, HIGH);
    delay(500);
    for(int i=P2LightStartPin;i<=P2LightStartPin+NumLights-1;i++)
    {
      digitalWrite(i, LOW);
    }
    digitalWrite(ScorePin, LOW);
    delay(500);
  }
  resetFunc();
}

void P1Win()
{
  AllLow(P1LightStartPin, P1LightStartPin+NumLights-1);
  AllLow(P2LightStartPin, P2LightStartPin+NumLights-1);
  for(int i = 0;i<5; i++)
  {
    for(int i=P1LightStartPin;i<=P1LightStartPin+NumLights-1;i++)
    {
      digitalWrite(i, HIGH);
    }
    digitalWrite(ScorePin, HIGH);
    delay(500);
    for(int i=P1LightStartPin;i<=P1LightStartPin+NumLights-1;i++)
    {
      digitalWrite(i, LOW);
    }
    digitalWrite(ScorePin, LOW);
    delay(500);
  }
  resetFunc();
}
