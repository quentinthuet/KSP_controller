//INCLUDES
#include <Wire.h> // Enable this line if using Arduino Uno, Mega, etc.
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"

//DEF 7SEGMENTS
Adafruit_7segment matrix70 = Adafruit_7segment();
Adafruit_7segment matrix71 = Adafruit_7segment();
Adafruit_7segment matrix72 = Adafruit_7segment();
Adafruit_7segment matrix73 = Adafruit_7segment();
Adafruit_7segment matrix74 = Adafruit_7segment();
Adafruit_7segment matrix75 = Adafruit_7segment();
Adafruit_7segment matrix76 = Adafruit_7segment();

//DEF VARS VITESSES ET ALTITUDES
int vitesse;  long apo_alt; long apo_time; long altitude; long peri_alt; long peri_time; int abovedixmille;

//DEF VARS RESSOURCES
int fuel_stage; int fuel_stage_max; int fuel_total; int fuel_total_max;
int monop_stage; int monop_stage_max; int monop_total; int monop_total_max;
int elec_stage; int elec_stage_max; int elec_total; int elec_total_max;

//DEF VARS BOUTONS
int etatBout2; int etatBout3;
int etatNowBout4; int etatLastBout4 = 9;
int etatNowBout5; int etatLastBout5 = 9;
int etatNowBout6; int etatLastBout6 = 9;
int etatNowBout12; int etatLastBout12 = 9;
int etatNowBout13; int etatLastBout13 = 9;
int etatNowBout14; int etatLastBout14 = 9;
int etatNowBout15; int etatLastBout15 = 9;
int etatNowBoutST; int etatLastBoutST = 9;
int etatNowBoutSV; int etatLastBoutSV = 9;
int etatNowBout16; int etatLastBout16 = 9;
int etatNowBout17; int etatLastBout17 = 9;
int etatNowBout18; int etatLastBout18 = 9;
int etatNowBout52; int etatLastBout52 = 9;
int etatNowBout53; int etatLastBout53 = 9;
int etatNowBoutA0; int etatLastBoutA0 = 9;

void setup(){
  
  //SERIAL
  Serial.begin(9600);
  
  //INIT 7SEGMENTS
  matrix70.begin(0x70);//rouge
  matrix71.begin(0x71);//jaune apo 1
  matrix72.begin(0x72);//jaune apo 2
  matrix73.begin(0x73);//vert 1
  matrix74.begin(0x74);//vert 2
  matrix75.begin(0x75);//jaune peri 1
  matrix76.begin(0x76);//jaune peri 2
 
  //INIT BOUTONS -> INPUT
  pinMode(2,INPUT_PULLUP);
  pinMode(3,INPUT_PULLUP);
  pinMode(4,INPUT_PULLUP);
  pinMode(5,INPUT_PULLUP);
  pinMode(6,INPUT_PULLUP);
  pinMode(12,INPUT_PULLUP);
  pinMode(13,INPUT_PULLUP);
  pinMode(14,INPUT_PULLUP);
  pinMode(15,INPUT_PULLUP);
  pinMode(50,INPUT_PULLUP);
  pinMode(19,INPUT_PULLUP);//STAGE
  pinMode(16,INPUT_PULLUP);
  pinMode(17,INPUT_PULLUP);
  pinMode(18,INPUT_PULLUP);
  pinMode(52,INPUT_PULLUP);
  pinMode(53,INPUT_PULLUP);
  pinMode(A0,INPUT_PULLUP);
  
  //INIT LEDS -> OUTPUT
  for (int i=7; i <= 11; i++){pinMode(i,OUTPUT);}
  for (int i=22; i <= 48; i++){pinMode(i,OUTPUT);}
  pinMode(49,OUTPUT); pinMode(51,OUTPUT);

  //ETAT DE DEPART
  //on affiche des traits sur les 7 segments
  matrix70.print(10000, DEC); matrix70.writeDisplay();
  matrix71.print(10000, DEC); matrix71.writeDisplay();
  matrix72.print(10000, DEC); matrix72.writeDisplay();
  matrix73.print(10000, DEC); matrix73.writeDisplay();
  matrix74.print(10000, DEC); matrix74.writeDisplay();
  matrix75.print(10000, DEC); matrix75.writeDisplay();
  matrix76.print(10000, DEC); matrix76.writeDisplay();
  //on allume les leds ressources
  for (int i=22; i <= 48; i++){digitalWrite(i, HIGH);}
  
}

void loop(){

  //LECTURE ETAT BOUTONS
  etatBout2 = digitalRead(2);
  etatBout3 = digitalRead(3);
  etatNowBout4 = digitalRead(4);
  etatNowBout5 = digitalRead(5);
  etatNowBout6 = digitalRead(6);
  etatNowBout12 = digitalRead(12);
  etatNowBout13 = digitalRead(13);
  etatNowBout14 = digitalRead(14);
  etatNowBout15 = digitalRead(15);
  etatNowBoutSV = digitalRead(50);
  etatNowBoutST = digitalRead(19);//STAGE
  etatNowBout16 = digitalRead(16);
  etatNowBout17 = digitalRead(17);
  etatNowBout18 = digitalRead(18);
  etatNowBout52 = digitalRead(52);
  etatNowBout53 = digitalRead(53);
  etatNowBoutA0 = digitalRead(A0);

  //SI ON A APPUYE SUR UN DES BOUTONS
  //BOUT MAP
  if(etatNowBout4 != etatLastBout4){Serial.println("boutMap"); etatLastBout4 = etatNowBout4; delay(50);}
  //BOUT NAVBALL
  if(etatNowBout5 != etatLastBout5){Serial.println("boutNavball"); etatLastBout5 = etatNowBout5; delay(50);}
  //BOUT NEXT VESSEL
  if(etatNowBout6 != etatLastBout6){Serial.println("boutNextVessel"); etatLastBout6 = etatNowBout6; delay(50);}
  //BOUT LETGO
  if(etatNowBout12 != etatLastBout12){
    if(etatNowBout12==1){Serial.println("boutLetGo");}
    etatLastBout12 = etatNowBout12; delay(50);}
  //BOUT GRAB
  if(etatNowBout13 != etatLastBout13){
    if(etatNowBout13==1){Serial.println("boutGrab");}
    etatLastBout13 = etatNowBout13; delay(50);}
  //BOUT BOARD
  if(etatNowBout14 != etatLastBout14){
    if(etatNowBout14==1){Serial.println("boutBoard");}
    etatLastBout14 = etatNowBout14; delay(50);}
  //BOUT JETPACK
  if(etatNowBout15 != etatLastBout15){Serial.println("boutJetpack"); etatLastBout15 = etatNowBout15; delay(50);}
  //BOUTS POTAR
  if(etatNowBout16 != etatLastBout16){
    if(etatNowBout16 == 1){Serial.println("AltOn");}
    else{Serial.println("AltOff");}
    etatLastBout16 = etatNowBout16;
    delay(50);
  }
  if(etatNowBout17 != etatLastBout17){
    if(etatNowBout17 == 1){Serial.println("TabOn");}
    else{Serial.println("TabOff");}
    etatLastBout17 = etatNowBout17;
    delay(50);
  }
  if(etatNowBout18 != etatLastBout18){
    if(etatNowBout18 == 1){Serial.println("EscOn");}
    else{Serial.println("EscOff");}
    etatLastBout18 = etatNowBout18;
    delay(50);
  }
  if(etatNowBout52 != etatLastBout52){
    if(etatNowBout52 == 1){Serial.println("F55On");}
    else{Serial.println("F55Off");}
    etatLastBout52 = etatNowBout52;
    delay(50);
  }
  if(etatNowBout53 != etatLastBout53){
    if(etatNowBout53 == 1){Serial.println("F99On");}
    else{Serial.println("F99Off");}
    etatLastBout53 = etatNowBout53;
    delay(50);
  }
  if(etatNowBoutA0 != etatLastBoutA0){
    if(etatNowBoutA0 == 1){Serial.println("CustOn");}
    else{Serial.println("CustOff");}
    etatLastBoutA0 = etatNowBoutA0;
    delay(50);
  }
  //BOUT STAGE
  if(etatNowBoutST != etatLastBoutST){
    if(etatNowBoutST == 1){
      Serial.println("boutST");
      //remise à zéro des leds fuel stage
      fuel_stage_max = NULL; fuel_total_max = NULL;
      for (int i=22; i <= 30; i++){digitalWrite(i, HIGH);}
    }
    etatLastBoutST = etatNowBoutST;
    delay(50);
  }
  //BOUT RESSOURCES STAGE/VESSEL
  if(etatNowBoutSV != etatLastBoutSV){
    for (int i=22; i <= 48; i++){digitalWrite(i, HIGH);}
    if(etatNowBoutSV==0){digitalWrite(49, HIGH); digitalWrite(51, LOW);}else{digitalWrite(49, LOW); digitalWrite(51, HIGH);}
    etatLastBoutSV = etatNowBoutSV;
    delay(50);
  }

  //------------------------------------------
  //LECTURE DES DATA TRANSMISES PAR PYTHON
  if (Serial.available() > 0) {
    
    vitesse = Serial.parseInt();
    matrix70.print(vitesse, DEC); matrix70.writeDisplay();
    Serial.read();  // consume delimiter

    apo_alt = Serial.parseInt();
    if(etatBout2 == 0 && apo_alt > 0){afficheDouble(apo_alt, matrix71, matrix72);}
    Serial.read();  // consume delimiter

    apo_time = Serial.parseInt();
    if(etatBout2 == 1 && apo_time > 0){afficheDoubleTime(apo_time, matrix71, matrix72);}
    Serial.read();  // consume delimiter
    
    altitude = Serial.parseInt();
    afficheDouble(altitude, matrix73, matrix74);
    Serial.read();  // consume delimiter

    peri_alt = Serial.parseInt();
    if(etatBout3 == 1 && peri_alt > 0){afficheDouble(peri_alt, matrix75, matrix76);}
    Serial.read();  // consume delimiter

    peri_time = Serial.parseInt();
    if(etatBout3 == 0 && peri_time > 0){afficheDoubleTime(peri_time, matrix75, matrix76);}
    Serial.read();  // consume delimiter

    abovedixmille = Serial.parseInt();
    if(abovedixmille == 1){digitalWrite(7, LOW); digitalWrite(8, HIGH); digitalWrite(9, LOW); digitalWrite(10, HIGH);}
    else{digitalWrite(7, HIGH); digitalWrite(8, LOW); digitalWrite(9, HIGH); digitalWrite(10, LOW);}
    Serial.read();  // consume delimiter

    float warp = Serial.parseInt();
    if(warp > 1){digitalWrite(11, HIGH);}else{digitalWrite(11, LOW);}
    Serial.read();// consume delimiter

    fuel_stage = Serial.parseInt();
    //matrix71.print(fuel_stage, DEC); matrix71.writeDisplay();
    Serial.read();// consume delimiter

    fuel_total = Serial.parseInt();
    //matrix72.print(fuel_total, DEC); matrix72.writeDisplay();
    Serial.read();  // consume delimiter

    monop_stage = Serial.parseInt();
    //matrix73.print(monop_stage, DEC); matrix73.writeDisplay();
    Serial.read();  // consume delimiter

    monop_total = Serial.parseInt();
    //matrix74.print(monop_total, DEC); matrix74.writeDisplay();
    Serial.read();  // consume delimiter
    
    elec_stage = Serial.parseInt();
    //matrix75.print(elec_stage, DEC); matrix75.writeDisplay();
    Serial.read();  // consume delimiter

    elec_total = Serial.parseInt();
    //matrix76.print(elec_total, DEC); matrix76.writeDisplay();
    Serial.read();  // consume delimiter

    //GESTION LEDS RESSOURCES DU STAGE ACTUEL
    if(etatNowBoutSV == 0){
      if(fuel_stage_max != NULL){
        if(digitalRead(30) == 1 && fuel_stage <= 0){digitalWrite(30, LOW);}
        else if(digitalRead(29) == 1 && fuel_stage < fuel_stage_max*1/9){digitalWrite(29, LOW);}
        else if(digitalRead(28) == 1 && fuel_stage < fuel_stage_max*2/9){digitalWrite(28, LOW);}
        else if(digitalRead(27) == 1 && fuel_stage < fuel_stage_max*3/9){digitalWrite(27, LOW);}
        else if(digitalRead(26) == 1 && fuel_stage < fuel_stage_max*4/9){digitalWrite(26, LOW);}
        else if(digitalRead(25) == 1 && fuel_stage < fuel_stage_max*5/9){digitalWrite(25, LOW);}
        else if(digitalRead(24) == 1 && fuel_stage < fuel_stage_max*6/9){digitalWrite(24, LOW);}
        else if(digitalRead(23) == 1 && fuel_stage < fuel_stage_max*7/9){digitalWrite(23, LOW);}
        else if(digitalRead(22) == 1 && fuel_stage < fuel_stage_max*8/9){digitalWrite(22, LOW);}
      }
      else{
        fuel_stage_max = fuel_stage;
        if(fuel_stage_max == 0){for (int i=22; i <= 30; i++){digitalWrite(i, LOW);}}
      }
      //MONOP STAGE
      if(monop_stage_max != NULL){
        if(digitalRead(39) == 1 && monop_stage <= 0){digitalWrite(39, LOW);}
        else if(digitalRead(38) == 1 && monop_stage < monop_stage_max*1/9){digitalWrite(38, LOW);}
        else if(digitalRead(37) == 1 && monop_stage < monop_stage_max*2/9){digitalWrite(37, LOW);}
        else if(digitalRead(36) == 1 && monop_stage < monop_stage_max*3/9){digitalWrite(36, LOW);}
        else if(digitalRead(35) == 1 && monop_stage < monop_stage_max*4/9){digitalWrite(35, LOW);}
        else if(digitalRead(34) == 1 && monop_stage < monop_stage_max*5/9){digitalWrite(34, LOW);}
        else if(digitalRead(33) == 1 && monop_stage < monop_stage_max*6/9){digitalWrite(33, LOW);}
        else if(digitalRead(32) == 1 && monop_stage < monop_stage_max*7/9){digitalWrite(32, LOW);}
        else if(digitalRead(31) == 1 && monop_stage < monop_stage_max*8/9){digitalWrite(31, LOW);}
      }
      else{
        monop_stage_max = monop_stage;
        if(monop_stage_max == 0){for (int i=31; i <= 39; i++){digitalWrite(i, LOW);}}
      }
      //ELEC STAGE
      if(elec_stage_max != NULL){
        if(digitalRead(48) == 1 && elec_stage <= 0){digitalWrite(48, LOW);}
        else if(digitalRead(47) == 1 && elec_stage < elec_stage_max*1/9){digitalWrite(47, LOW);}
        else if(digitalRead(46) == 1 && elec_stage < elec_stage_max*2/9){digitalWrite(46, LOW);}
        else if(digitalRead(45) == 1 && elec_stage < elec_stage_max*3/9){digitalWrite(45, LOW);}
        else if(digitalRead(44) == 1 && elec_stage < elec_stage_max*4/9){digitalWrite(44, LOW);}
        else if(digitalRead(43) == 1 && elec_stage < elec_stage_max*5/9){digitalWrite(43, LOW);}
        else if(digitalRead(42) == 1 && elec_stage < elec_stage_max*6/9){digitalWrite(42, LOW);}
        else if(digitalRead(41) == 1 && elec_stage < elec_stage_max*7/9){digitalWrite(41, LOW);}
        else if(digitalRead(40) == 1 && elec_stage < elec_stage_max*8/9){digitalWrite(40, LOW);}
      }
      else{
        elec_stage_max = elec_stage;
        if(elec_stage_max == 0){for (int i=40; i <= 48; i++){digitalWrite(i, LOW);}}
      }
    }

    //GESTION LEDS RESSOURCES TOTAL
    else if(etatNowBoutSV == 1){
      if(fuel_total_max != NULL){
        if(digitalRead(30) == 1 && fuel_total <= 0){digitalWrite(30, LOW);}
        else if(digitalRead(29) == 1 && fuel_total < fuel_total_max*1/9){digitalWrite(29, LOW);}
        else if(digitalRead(28) == 1 && fuel_total < fuel_total_max*2/9){digitalWrite(28, LOW);}
        else if(digitalRead(27) == 1 && fuel_total < fuel_total_max*3/9){digitalWrite(27, LOW);}
        else if(digitalRead(26) == 1 && fuel_total < fuel_total_max*4/9){digitalWrite(26, LOW);}
        else if(digitalRead(25) == 1 && fuel_total < fuel_total_max*5/9){digitalWrite(25, LOW);}
        else if(digitalRead(24) == 1 && fuel_total < fuel_total_max*6/9){digitalWrite(24, LOW);}
        else if(digitalRead(23) == 1 && fuel_total < fuel_total_max*7/9){digitalWrite(23, LOW);}
        else if(digitalRead(22) == 1 && fuel_total < fuel_total_max*8/9){digitalWrite(22, LOW);}
      }
      else{
        fuel_total_max = fuel_total;
        if(fuel_total_max == 0){for (int i=22; i <= 30; i++){digitalWrite(i, LOW);}}
      }
      //MONOP TOTAL
       if(monop_total_max != NULL){
        if(digitalRead(39) == 1 && monop_total <= 0){digitalWrite(39, LOW);}
        else if(digitalRead(38) == 1 && monop_total < monop_total_max*1/9){digitalWrite(38, LOW);}
        else if(digitalRead(37) == 1 && monop_total < monop_total_max*2/9){digitalWrite(37, LOW);}
        else if(digitalRead(36) == 1 && monop_total < monop_total_max*3/9){digitalWrite(36, LOW);}
        else if(digitalRead(35) == 1 && monop_total < monop_total_max*4/9){digitalWrite(35, LOW);}
        else if(digitalRead(34) == 1 && monop_total < monop_total_max*5/9){digitalWrite(34, LOW);}
        else if(digitalRead(33) == 1 && monop_total < monop_total_max*6/9){digitalWrite(33, LOW);}
        else if(digitalRead(32) == 1 && monop_total < monop_total_max*7/9){digitalWrite(32, LOW);}
        else if(digitalRead(31) == 1 && monop_total < monop_total_max*8/9){digitalWrite(31, LOW);}
      }
      else{
        monop_total_max = monop_total;
        if(monop_total_max == 0){for (int i=31; i <= 39; i++){digitalWrite(i, LOW);}}
      }
      //ELEC TOTAL
       if(elec_total_max != NULL){
        if(digitalRead(48) == 1 && elec_total <= 0){digitalWrite(48, LOW);}
        else if(digitalRead(47) == 1 && elec_total < elec_total_max*1/9){digitalWrite(47, LOW);}
        else if(digitalRead(46) == 1 && elec_total < elec_total_max*2/9){digitalWrite(46, LOW);}
        else if(digitalRead(45) == 1 && elec_total < elec_total_max*3/9){digitalWrite(45, LOW);}
        else if(digitalRead(44) == 1 && elec_total < elec_total_max*4/9){digitalWrite(44, LOW);}
        else if(digitalRead(43) == 1 && elec_total < elec_total_max*5/9){digitalWrite(43, LOW);}
        else if(digitalRead(42) == 1 && elec_total < elec_total_max*6/9){digitalWrite(42, LOW);}
        else if(digitalRead(41) == 1 && elec_total < elec_total_max*7/9){digitalWrite(41, LOW);}
        else if(digitalRead(40) == 1 && elec_total < elec_total_max*8/9){digitalWrite(40, LOW);}
      }
      else{
        elec_total_max = elec_total;
        if(elec_total_max == 0){for (int i=40; i <= 48; i++){digitalWrite(i, LOW);}}
      }
    }
    
  }
  //FIN LECTURE DES DATA TRANSMISES PAR PYTHON
  //------------------------------------------
  
}


//FONTION POUR AFFICHER SUR 2 CADRANS AVEC POINT AU MILLIERS
void afficheDouble(long datarecu, Adafruit_7segment cadran1, Adafruit_7segment cadran2){

    //au dessus de 10 000 : affichage sur les 2 cadrans
    if(datarecu > 9999){

      //cadran gauche
      int data1 = int(datarecu / 10000);
      cadran1.print(data1, DEC);
      if(data1 > 99){cadran1.writeDigitNum(1, (data1 / 100), true);}//ajout du point décimal n°2
      cadran1.writeDisplay();//affichage des dizaine de milliers
      
      //cadran droite
      int data2 = datarecu - (data1 * 10000);
      cadran2.print(data2);
      cadran2.writeDigitNum(0, (data2 / 1000), true);//ajout du point décimal
      cadran2.writeDisplay();
            
    }

    //en dessous de 10 000 : affichage sur un seul cadran + on efface autre cadran
    else if(datarecu >= 0){
      cadran1.print(10000, DEC); cadran1.writeDisplay();//on efface le cadran 1
      
      cadran2.print(datarecu, DEC);
      cadran2.writeDigitNum(0, (datarecu / 1000), true);//ajout du point décimal
      if(datarecu < 10){cadran2.writeDigitNum(3, 0);}//zéro supplémentaires si besoin
      if(datarecu < 100){cadran2.writeDigitNum(1, 0);}//zéro supplémentaires si besoin
      cadran2.writeDisplay();
    }

     //données incoherente : on efface
    else{cadran1.print(10000, DEC); cadran1.writeDisplay();cadran2.print(10000, DEC); cadran2.writeDisplay();}
    
}


//FONTION POUR AFFICHER SUR 2 CADRANS POUR LES TIMING
void afficheDoubleTime(long datarecu, Adafruit_7segment cadran1, Adafruit_7segment cadran2){

    //au dessus de 1h : affichage sur les 2 cadrans
    if(datarecu > 3599){

      //cadran gauche
      int datadays = int(datarecu / 86400);
      int datahours = int((datarecu - (datadays * 86400))/3600);
      int tout1 = (datadays*100) + datahours;
      cadran1.print(tout1);
      cadran1.drawColon(true);//ajout du deux points
      if(tout1 < 10){cadran1.writeDigitNum(3, 0);}//zéro supplémentaires si besoin
      if(tout1 < 100){cadran1.writeDigitNum(1, 0);}//zéro supplémentaires si besoin
      if(tout1 < 1000){cadran1.writeDigitNum(0, 0);}//zéro supplémentaires si besoin
      cadran1.writeDigitNum(4, datahours-int(datahours/10), true);//ajout du point décimal
      cadran1.writeDisplay();
      
      //cadran droite
      int datamin = int((datarecu - (datadays * 86400) - (datahours * 3600))/60);
      int datasec = int(datarecu - (datadays * 86400) - (datahours * 3600) - (datamin*60));
      int tout = (datamin*100) + datasec;
      cadran2.print(tout);
      cadran2.drawColon(true);//ajout du deux points
      if(tout < 10){cadran2.writeDigitNum(3, 0);}//zéro supplémentaires si besoin
      if(tout < 100){cadran2.writeDigitNum(1, 0);}//zéro supplémentaires si besoin
      if(tout < 1000){cadran2.writeDigitNum(0, 0);}//zéro supplémentaires si besoin
      cadran2.writeDisplay();
            
    }

    //en dessous de 1h : affichage sur un seul cadran + on efface autre cadran
    else if(datarecu >= 0){
      cadran1.print(10000, DEC); cadran1.writeDisplay();//on efface le cadran 1
      
      int datamin = int(datarecu / 60);
      int datasec = datarecu - (datamin * 60);
      int tout = (datamin*100) + datasec;
      cadran2.print(tout);
      cadran2.drawColon(true);//ajout du deux points
      if(tout < 10){cadran2.writeDigitNum(3, 0);}//zéro supplémentaires si besoin
      if(tout < 100){cadran2.writeDigitNum(1, 0);}//zéro supplémentaires si besoin
      if(tout < 1000){cadran2.writeDigitNum(0, 0);}//zéro supplémentaires si besoin
      cadran2.writeDisplay();
    }

    //données incoherente : on efface
    else{cadran1.print(10000, DEC); cadran1.writeDisplay();cadran2.print(10000, DEC); cadran2.writeDisplay();}
    
}
