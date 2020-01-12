int latch=12;  //74HC595  pin 9 STCP
int clock=13; //74HC595  pin 10 SHCP
int data=11;   //74HC595  pin 8 DS
int current_speed = 0;
unsigned char table[]=
{0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c
,0x39,0x5e,0x79,0x71,0x00};

void setup() {
  pinMode(latch,OUTPUT);
  pinMode(clock,OUTPUT);
  pinMode(data,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Lecture Python //
  
  while(Serial.available()) {
    current_speed = Serial.parseInt();
    Serial.read();
  }
  Display(current_speed);
  delay(100);
}

void Display(unsigned char num)
{
  digitalWrite(latch,LOW);
  shiftOut(data,clock,MSBFIRST,table[num]);
  digitalWrite(latch,HIGH); 
}
