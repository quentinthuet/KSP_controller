//PINS DE 2 à 12 + A3 à A5
const int pin2 = 2; int etatNowBout2 = 0; int etatLastBout2 = 0;
const int pin3 = 3; int etatNowBout3 = 0; int etatLastBout3 = 0;
const int pin4 = 4; int etatNowBout4 = 0; int etatLastBout4 = 0;
const int pin5 = 5; int etatNowBout5 = 0; int etatLastBout5 = 0;
const int pin6 = 6; int etatNowBout6 = 0; int etatLastBout6 = 0;
const int pin7 = 7; int etatNowBout7 = 0; int etatLastBout7 = 0;
const int pin8 = 8; int etatNowBout8 = 0; int etatLastBout8 = 0;
const int pin9 = 9; int etatNowBout9 = 0; int etatLastBout9 = 0;
const int pin10 = 10; int etatNowBout10 = 0; int etatLastBout10 = 0;
const int pin11 = 11; int etatNowBout11 = 0; int etatLastBout11 = 0;
const int pin12 = 12; int etatNowBout12 = 0; int etatLastBout12 = 0;
const int pinA3 = A3; int etatNowBoutA3 = 0; int etatLastBoutA3 = 0;
const int pinA4 = A4; int etatNowBoutA4 = 0; int etatLastBoutA4 = 0;
const int pinA5 = A5; int etatNowBoutA5 = 0; int etatLastBoutA5 = 0;
//THROTTLE
const int pinTH = A1; int etatNowBoutTH = 0; int etatLastBoutTH = 0;
//STAGE
//const int pinST = A1; int etatNowBoutST = 0; int etatLastBoutST = 0;

void setup()
{
Serial.begin(9600);
pinMode(pin2,INPUT_PULLUP);
pinMode(pin3,INPUT_PULLUP);
pinMode(pin4,INPUT_PULLUP);
pinMode(pin5,INPUT_PULLUP);
pinMode(pin6,INPUT_PULLUP);
pinMode(pin7,INPUT_PULLUP);
pinMode(pin8,INPUT_PULLUP);
pinMode(pin9,INPUT_PULLUP);
pinMode(pin10,INPUT_PULLUP);
pinMode(pin11,INPUT_PULLUP);
pinMode(pin12,INPUT_PULLUP);
pinMode(pinA3,INPUT_PULLUP);
pinMode(pinA4,INPUT_PULLUP);
pinMode(pinA5,INPUT_PULLUP);
//THROTTLE
pinMode(pinTH,INPUT_PULLUP);
//STAGE
//pinMode(pinST,INPUT_PULLUP);
pinMode(A0,OUTPUT);
}


void loop()
{

etatNowBout2 = digitalRead(pin2);
etatNowBout3 = digitalRead(pin3);
etatNowBout4 = digitalRead(pin4);
etatNowBout5 = digitalRead(pin5);
etatNowBout6 = digitalRead(pin6);
etatNowBout7 = digitalRead(pin7);
etatNowBout8 = digitalRead(pin8);
etatNowBout9 = digitalRead(pin9);
etatNowBout10 = digitalRead(pin10);
etatNowBout11 = digitalRead(pin11);
etatNowBout12 = digitalRead(pin12);
etatNowBoutA3 = digitalRead(pinA3);
etatNowBoutA4 = digitalRead(pinA4);
etatNowBoutA5 = digitalRead(pinA5);
//THROTTLE
etatNowBoutTH = analogRead(pinTH);
//STAGE
//etatNowBoutST = digitalRead(pinST);

if(etatNowBout2 != etatLastBout2){Serial.println("bout2"); etatLastBout2 = etatNowBout2; delay(50);}
else if(etatNowBout3 != etatLastBout3){Serial.println("bout3"); etatLastBout3 = etatNowBout3; delay(50);}
else if(etatNowBout4 != etatLastBout4){Serial.println("bout4"); etatLastBout4 = etatNowBout4; delay(50);}
else if(etatNowBout5 != etatLastBout5){Serial.println("bout5"); etatLastBout5 = etatNowBout5; delay(50);}
else if(etatNowBout6 != etatLastBout6){Serial.println("bout6"); etatLastBout6 = etatNowBout6; delay(50);}
else if(etatNowBout7 != etatLastBout7){Serial.println("bout7"); etatLastBout7 = etatNowBout7; delay(50);}
else if(etatNowBout8 != etatLastBout8){Serial.println("bout8"); etatLastBout8 = etatNowBout8; delay(50);}
else if(etatNowBout9 != etatLastBout9){Serial.println("bout9"); etatLastBout9 = etatNowBout9; delay(50);}
else if(etatNowBout10 != etatLastBout10){Serial.println("bout10"); etatLastBout10 = etatNowBout10; delay(50);}
else if(etatNowBout11 != etatLastBout11){Serial.println("bout11"); etatLastBout11 = etatNowBout11; delay(50);}
else if(etatNowBout12 != etatLastBout12){Serial.println("bout12"); etatLastBout12 = etatNowBout12; delay(50);}
else if(etatNowBoutA3 != etatLastBoutA3){Serial.println("boutA3"); etatLastBoutA3 = etatNowBoutA3; delay(50);}
else if(etatNowBoutA4 != etatLastBoutA4){Serial.println("boutA4"); etatLastBoutA4 = etatNowBoutA4; delay(50);}
else if(etatNowBoutA5 != etatLastBoutA5){Serial.println("boutA5"); etatLastBoutA5 = etatNowBoutA5; delay(50);}
//THROTTLE
else if(etatNowBoutTH > etatLastBoutTH+10 || etatNowBoutTH < etatLastBoutTH-10){
  //else if(etatNowBoutTH != etatLastBoutTH){
  Serial.println(etatNowBoutTH); etatLastBoutTH = etatNowBoutTH;
  if(etatNowBoutTH > 50){digitalWrite(A0, HIGH);}else{digitalWrite(A0, LOW);}
  delay(100);
  }
//STAGE
//else if(etatNowBoutST != etatLastBoutST){
  //if(etatNowBoutST == 1){Serial.println("boutST");}
   //etatLastBoutST = etatNowBoutST;
   //delay(50);
 //}

}
