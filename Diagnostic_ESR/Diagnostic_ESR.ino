//Purpose:    To create an AC frequency and DC sweep while intaking data from the ESR
//Author:     Max Kingsley
//Data:       March 9 2022


int acPin = 9;            //Calls pins for AC. 10 is virtual ground and 9 is the signal
int virgrd = 10;
double val = 0;
int freq = 1000;
double t = 0;
const double pi = 3.1415;
const double fs = 1000;

int sweepPin = 2;         //pin used for sweep. currently a set dc voltage, and does not sweep.
int sweep = 0;
int sweepSet = 41;
int output = 0;

int sweepCounter = 0;

void setup() {

//Serial.begin(19200);
pinMode(acPin,OUTPUT);
//pinMode(sweepPin,OUTPUT);

analogWrite(sweepPin, 512);   //sets sweep to 2.5V

}

void loop() {

t = millis();                 //provides the function for the AC signal, constantly changes
val = 127*sin(2*pi*(freq)*t)+127;
analogWrite(acPin,val);
analogWrite(virgrd,127);

}
