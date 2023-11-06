#include <Servo.h>

Servo servo1;

const int NumLights = 3;

const int P1LightStartPin = 11;   //relevent payers, their button pins and the relevant first pin on the shift register which controls their first light
const int P1ButPin = 6;

const int P2LightStartPin = 8;
const int P2ButPin = 5;

const int P3LightStartPin = 1;
const int P3ButPin = 7;

const int ScorePin = 9; // pin declarations for various components. use of const to make debugging easier and for security

const int ServoPin = 10; 

const int PotPin = A0;

const int BuzzPin = 11;

int MaxTime;
const int MinDelay = 200; //score relevant variables
const int MaxDelay = 1500;
const int ScoreDelay = 50;
const int MaxScore = 10;
int CurrHighScore = 1; // which player has the current highest score

const int MaxNegDelay = 250;

int BuzzDelay = 0;

int P1WaitDelay = 0; // player relevant delays
int P2WaitDelay = 0;
int P3WaitDelay = 0;

int P1NegDelay = 0;
int P2NegDelay = 0;
int P3NegDelay = 0;

bool P1Scored = true;
bool P2Scored = true;
bool P3Scored = true;

int P1CurrTime = 0;
int P2CurrTime = 0;
int P3CurrTime = 0;

int P1CurrLightOn = -1;
int P2CurrLightOn = -1;
int P3CurrLightOn = -1;

int P1Score = 0;
int P2Score = 0;
int P3Score = 0;

const int ClockPin = 4; // pins for the shift registers
const int LatchPin = 3;
const int DataPin = 2;

const int BuzzFreq = 100;

//Title: Arduino-74HC595-shift-registers
//Author: janisrove
//Date: 2015
//Code Version: 1.0
//Available from: https://github.com/janisrove/Arduino-74HC595-shift-registers/blob/master/ArduinoLEDsWithShiftRegisters/ArduinoLEDsWithShiftRegisters.ino
//Access date: 31 October 2023 

int numOfRegisters = 2;
byte* registerState;

long effectId = 0;
long prevEffect = 0;
long effectRepeat = 0;
long effectSpeed = 30;

//End of citation


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(P1ButPin, INPUT); // initialising all needed pins
  pinMode(P2ButPin, INPUT);
  pinMode(P3ButPin, INPUT);

  pinMode(ScorePin, OUTPUT);

  digitalWrite(LatchPin, HIGH);

  pinMode(LatchPin, OUTPUT);
  pinMode(ClockPin, OUTPUT);
  pinMode(DataPin, OUTPUT);

  servo1.attach(ServoPin);

  pinMode(BuzzPin, OUTPUT);

  //Title: Arduino-74HC595-shift-registers
  //Author: janisrove
  //Date: 2015
  //Code Version: 1.0
  //Available from: https://github.com/janisrove/Arduino-74HC595-shift-registers/blob/master/ArduinoLEDsWithShiftRegisters/ArduinoLEDsWithShiftRegisters.ino
  //Access date: 31 October 2023 

  //Initialize array
  registerState = new byte[numOfRegisters];
	for (size_t i = 0; i < numOfRegisters; i++) {
		registerState[i] = 0;
	}
  
  //End of citation 
}

void loop() {
  // put your main code here, to run repeatedly:  
  servo1.write(180-(50*CurrHighScore)); // Calculating and outputting servo direction

  MaxTime = analogRead(PotPin) + 100; // Cifficulty calculation

  if (P1CurrTime>=MaxTime && P1WaitDelay<=0) // Displaying a new pin if the time has been exceeded
  {
    if (!P1Scored)
    {
      regWrite(P1LightStartPin + P1CurrLightOn, LOW);
      P1Scored = true;
      P1WaitDelay = rand()%(MaxDelay-MinDelay) + MinDelay;
    } else
    {
      P1Scored = false;
    
      P1CurrTime=0;
      int RandomNum = rand() % NumLights;
      P1CurrLightOn = RandomNum;
      regWrite(P1LightStartPin + P1CurrLightOn, HIGH);
    }
  }

  if(digitalRead(P1ButPin)==HIGH && P1WaitDelay <= 0) // checking if a pin has been scored and scoring if it has
  {
    P1Scored=true;
    P1ScorePoint(1);
    P1CurrTime=MaxTime;
    regWrite(P1LightStartPin + P1CurrLightOn, LOW);
    P1WaitDelay = rand()%(MaxDelay-MinDelay) + MinDelay;
    P1NegDelay = MaxNegDelay;
  }


  if (P2CurrTime>=MaxTime && P2WaitDelay<=0) // Repeat of P1 for P2 and P3, could be concatenated using references to variables if refactored
  {
    if (!P2Scored)
    {
      regWrite(P2LightStartPin + P2CurrLightOn, LOW);
      P2Scored = true;
      P2WaitDelay = rand()%(MaxDelay-MinDelay) + MinDelay;
    } else
    {
      P2Scored = false;
      P2CurrTime=0;
      int RandomNum = rand() % NumLights;
      P2CurrLightOn = RandomNum;
      regWrite(P2LightStartPin + P2CurrLightOn, HIGH);
    }
  }

  if(digitalRead(P2ButPin)==HIGH && P2WaitDelay<=0)
  {
    P2Scored = true;
    P2ScorePoint(1);
    P2CurrTime=MaxTime;
    regWrite(P2LightStartPin + P2CurrLightOn, LOW);
    P2WaitDelay = rand()%(MaxDelay-MinDelay) + MinDelay;
    P2NegDelay = MaxNegDelay;
  }

  if (P3CurrTime>=MaxTime && P3WaitDelay<=0)
  {
    if (!P3Scored)
    {
      regWrite(P3LightStartPin + P3CurrLightOn, LOW);
      P3Scored = true;
      P3WaitDelay = rand()%(MaxDelay-MinDelay) + MinDelay;
    } else
    {
      P3Scored = false;
      P3CurrTime=0;
      int RandomNum = rand() % NumLights;
      P3CurrLightOn = RandomNum;
      regWrite(P3LightStartPin + P3CurrLightOn, HIGH);
    }
  }

  if(digitalRead(P3ButPin)==HIGH && P3WaitDelay <= 0)
  {
    P3Scored=true;
    P3ScorePoint(1);
    P3CurrTime=MaxTime;
    regWrite(P3LightStartPin + P3CurrLightOn, LOW);
    P3WaitDelay = rand()%(MaxDelay-MinDelay) + MinDelay;
    P3NegDelay = MaxNegDelay;
  }

  if (P1NegDelay<=0 && P1WaitDelay>0 && digitalRead(P1ButPin)==HIGH) // check to see if a button if pressed with no light on, repeated for P2 and P3, could also be refactored using references
  {
    P1ScorePoint(-2);
    P1NegDelay = MaxNegDelay;
  }
   if (P2NegDelay<=0 && P2WaitDelay>0 && digitalRead(P2ButPin)==HIGH)
  {
    P2ScorePoint(-2);
    P2NegDelay = MaxNegDelay;
  }

   if (P3NegDelay<=0 && P3WaitDelay>0 && digitalRead(P3ButPin)==HIGH)
  {
    P3ScorePoint(-2);
    P3NegDelay = MaxNegDelay;
  }

  P1CurrTime++; // iterating through relevant iterators
  P2CurrTime++;
  P3CurrTime++;

  P1WaitDelay--;
  P2WaitDelay--;
  P3WaitDelay--;

  P1NegDelay--;
  P2NegDelay--;
  P3NegDelay--;
  
  BuzzDelay --;

  if (BuzzDelay == 0) // Checking to see if all iterators are positive to avoid overflow/overflow issues
  {
    noTone(BuzzPin);
  }
  if (BuzzDelay <0)
  {
    BuzzDelay = 0;
  }

  if (P1CurrTime<0)
  {
    P1CurrTime = 0;
  }
  if (P2CurrTime<0)
  {
    P2CurrTime = 0;
  }
  if (P3CurrTime<0)
  {
    P3CurrTime = 0;
  }

  if (P1WaitDelay<0)
  {
    P1WaitDelay = 0;
  }
  if (P2WaitDelay<0)
  {
    P2WaitDelay = 0;
  }
  if (P3WaitDelay<0)
  {
    P3WaitDelay = 0;
  }

  if (P1NegDelay<0)
  {
    P1NegDelay = 0;
  }
  if (P2NegDelay<0)
  {
    P2NegDelay = 0;
  }
  if (P3NegDelay<0)
  {
    P3NegDelay = 0;
  }

  delay(1);
}

void(* resetFunc) (void) = 0; // Restart progran

void P1ScorePoint(int points) // Score points for P1 and show correct lights/sounds, copied for P2 and P3, could be refactored
{
  P1Score += points;
  digitalWrite((ScorePin), HIGH);
  delay(ScoreDelay);
  digitalWrite((ScorePin), LOW);
  Serial.println("P1 Score: ");
  Serial.println(P1Score);
  
  if((P1Score>=P2Score) && (P1Score>=P3Score))
  {
    CurrHighScore = 1;
  }
  if (P1Score>=MaxScore)
  {
    P1Win();
  }
  tone(BuzzPin,BuzzFreq);
  BuzzDelay = 50;
}
void P2ScorePoint(int points)
{
  P2Score += points;
  digitalWrite((ScorePin), HIGH);
  delay(ScoreDelay);
  digitalWrite((ScorePin), LOW);
  Serial.println("P2 Score: ");
  Serial.println(P2Score);
  if((P2Score>=P1Score) && (P2Score>=P3Score))
  {
    CurrHighScore = 2;
  }
  if (P2Score>=MaxScore)
  {
    P2Win();
  }
  tone(BuzzPin,BuzzFreq);
  BuzzDelay = 50;
}

void P3ScorePoint(int points)
{
  P3Score += points;
  digitalWrite((ScorePin), HIGH);
  delay(ScoreDelay);
  digitalWrite((ScorePin), LOW);
  Serial.println("P3 Score: ");
  Serial.println(P3Score);
  if((P3Score>=P2Score) && (P3Score>=P1Score))
  {
    CurrHighScore = 3;
  }
  if (P3Score>=MaxScore)
  {
    P3Win();
  }
  tone(BuzzPin,BuzzFreq);
  BuzzDelay = 50;
}

void P2Win() // if P2 wins then flash lights and play buzzer, copied for P1, P3, could be refactored
{
  tone(BuzzPin,BuzzFreq);
   for (int k = 0; k<NumLights; k++)
    {
      regWrite(P2LightStartPin+k, LOW);
    }
  for (int k = 0; k<NumLights; k++)
    {
      regWrite(P1LightStartPin+k, LOW);
    }
    for (int k = 0; k<NumLights; k++)
    {
      regWrite(P3LightStartPin+k, LOW);
    }
  for(int i = 0;i<5; i++)
  {
    for (int k = 0; k<NumLights; k++)
    {
      regWrite(P2LightStartPin+k, OUTPUT);
    }
    digitalWrite(ScorePin, HIGH);
    delay(500);

    for (int k = 0; k<NumLights; k++)
    {
      regWrite(P2LightStartPin+k, LOW);
    }
    digitalWrite(ScorePin, LOW);
    delay(500);

  }
  noTone(BuzzPin);
  resetFunc();
}

void P1Win()
{
  tone(BuzzPin,BuzzFreq);
  for (int k = 0; k<NumLights; k++)
    {
      regWrite(P2LightStartPin+k, LOW);
    }
  for (int k = 0; k<NumLights; k++)
    {
      regWrite(P1LightStartPin+k, LOW);
    }
    for (int k = 0; k<NumLights; k++)
    {
      regWrite(P3LightStartPin+k, LOW);
    }
  for(int i = 0;i<5; i++)
  {
    for (int k = 0; k<NumLights; k++)
    {
      regWrite(P1LightStartPin+k, OUTPUT);
    }
    digitalWrite(ScorePin, HIGH);
    delay(500);

    for (int k = 0; k<NumLights; k++)
    {
      regWrite(P1LightStartPin+k, LOW);
    }
    digitalWrite(ScorePin, LOW);
    delay(500);

  }
  resetFunc();
}

void P3Win()
{
  tone(BuzzPin,BuzzFreq);
  for (int k = 0; k<NumLights; k++)
    {
      regWrite(P2LightStartPin+k, LOW);
    }
  for (int k = 0; k<NumLights; k++)
    {
      regWrite(P1LightStartPin+k, LOW);
    }
  for (int k = 0; k<NumLights; k++)
    {
      regWrite(P3LightStartPin+k, LOW);
    }
  for(int i = 0;i<5; i++)
  {
    for (int k = 0; k<NumLights; k++)
    {
      regWrite(P3LightStartPin+k, OUTPUT);
    }
    digitalWrite(ScorePin, HIGH);
    delay(500);

    for (int k = 0; k<NumLights; k++)
    {
      regWrite(P3LightStartPin+k, LOW);
    }
    digitalWrite(ScorePin, LOW);
    delay(500);

  }
  noTone(BuzzPin);
  resetFunc();
}

 // code for accessing more than one register

//Title: Arduino-74HC595-shift-registers
//Author: janisrove
//Date: 2015
//Code Version: 1.0
//Available from: https://github.com/janisrove/Arduino-74HC595-shift-registers/blob/master/ArduinoLEDsWithShiftRegisters/ArduinoLEDsWithShiftRegisters.ino
//Access date: 31 October 2023 

void regWrite(int pin, bool state){
	//Determines register
	int reg = pin / 8;
	//Determines pin for actual register
	int actualPin = pin - (8 * reg);

	//Begin session
	digitalWrite(LatchPin, LOW);

	for (int i = 0; i < numOfRegisters; i++){
		//Get actual states for register
		byte* states = &registerState[i];

		//Update state
		if (i == reg){
			bitWrite(*states, actualPin, state);
		}

		//Write
		shiftOut(DataPin, ClockPin, MSBFIRST, *states);
	}

	//End session
	digitalWrite(LatchPin, HIGH);
}

//End of citation