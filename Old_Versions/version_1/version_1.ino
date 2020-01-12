int rcs, sas, abort_seq, solar_panel, throttle;
bool abort_seq_on, bouton_2_on, bouton_3_on, bouton_4_on, bouton_5_on, bouton_6_on;


void setup() {
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  digitalWrite(7,1);
  digitalWrite(8,1);
  digitalWrite(9,1);
  digitalWrite(10,1);
  Serial.begin(9600);
}

void loop() {
  // Lecture Pin //
  bouton_2_on = !(digitalRead(2));
  bouton_3_on = !(digitalRead(3));
  bouton_4_on = !(digitalRead(4));
  bouton_5_on = !(digitalRead(5));
  bouton_6_on = !(digitalRead(6));

  if (bouton_2_on) {
    Serial.println("seq"); 
    delay(100);
  }
  else if (bouton_3_on) {
    Serial.println("rcs"); 
    delay(100);
  }
  else if (bouton_4_on) {
    Serial.println("sas"); 
    delay(100);
  }
  else if (bouton_5_on) {
    Serial.println("abort"); 
    delay(100);
  }
  else if (bouton_6_on) {
    Serial.println("solar_panels"); 
    delay(100);
  }
  else {
    Serial.println("no_action");
    delay(50);
  }
  Serial.println(String(analogRead(0)));
  delay(50);  
  Serial.println(String(analogRead(1)));
  delay(50);  
  Serial.println(String(analogRead(2)));
  delay(50);
  // Lecture Python //
  
  while(Serial.available()) {
    rcs = Serial.parseInt();
    Serial.read();
    sas = Serial.parseInt();
    Serial.read();         
    abort_seq = Serial.parseInt();
    Serial.read();         
    solar_panel = Serial.parseInt();
    Serial.read();
    
    if (rcs == 0) {
      digitalWrite(7,1);
    }
    else if (rcs == 1) {
      digitalWrite(7,0);
    }
    if (sas == 0) {
      digitalWrite(8,1);
    }
    else if (sas == 1) {
      digitalWrite(8,0);
    }    
    if (!abort_seq_on && abort_seq == 1) {
      digitalWrite(9,0);
      abort_seq_on == true;
    }   
    if (solar_panel == 0) {
      digitalWrite(10,1);
    }
    else if (solar_panel == 1) {
      digitalWrite(10,0);
    }
  }
}
