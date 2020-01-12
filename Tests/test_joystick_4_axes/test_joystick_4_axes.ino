int reverser;
bool bouton_11_on;


void setup() {
  //pinMode(11, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  // Lecture Pin //
  /*bouton_11_on = !(digitalRead(11));

  if (bouton_11_on) {
    Serial.println("reverse"); 
    delay(100);
  }
  else {
    Serial.println("no_action");
    delay(50);
  }*/
  Serial.println(String(analogRead(3)));
  delay(50);  
  Serial.println(String(analogRead(4)));
  delay(50);  
  Serial.println(String(analogRead(5)));
  delay(50);
  
}
