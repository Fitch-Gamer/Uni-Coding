int const NumLights = 3;

int const LightStartPin = 2;
int const ButStartPin = 8;
int const ScorePin = 13;

int MaxTime = 1000;
int CurrTime = 0;
int CurrLightOn = -1;

int Score = 0;

int MinDelay = 200;
int MaxDelay = 1500;
int ScoreDelay = 50;

//int LightPins[NumLights];
//int ButPins[NumLights];


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  InitAll(LightStartPin, LightStartPin+NumLights-1,OUTPUT);
  InitAll(ButStartPin, ButStartPin+NumLights, INPUT);
  pinMode(ScorePin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (CurrTime>=MaxTime)
  {
    CurrTime=0;
    AllLow(LightStartPin, LightStartPin+NumLights-1);
    int RandomNum = rand() % NumLights;
    CurrLightOn = RandomNum;
    digitalWrite((RandomNum+LightStartPin), HIGH);
  }

  if(digitalRead(CurrLightOn+ButStartPin)==HIGH)
  {
    ScorePoint(1);
    CurrTime=MaxTime;
    AllLow(LightStartPin, LightStartPin+NumLights-1);
    Serial.println(Score);
    delay(rand()%(MaxDelay-MinDelay) + MinDelay);
  }
  CurrTime++;
  delay(1);
}

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
void ScorePoint(int points)
{
  Score += points;
  digitalWrite((ScorePin), HIGH);
  delay(ScoreDelay);
  digitalWrite((ScorePin), LOW);

}