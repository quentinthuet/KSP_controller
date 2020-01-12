

void setup() {
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
  pinMode(25, OUTPUT);
  pinMode(27, OUTPUT);
  pinMode(29, OUTPUT);
  digitalWrite(25,1);
  digitalWrite(27,1);
  digitalWrite(29,1);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (digitalRead(5) == 0) {
    Serial.print("0");
  }
  else {
    Serial.print("1");
  }
  if (digitalRead(6) == 0) {
    Serial.print("0");
  }
  else {
    Serial.print("1");
  }
  if (digitalRead(7) == 0) {
    Serial.print("0");
  }
  else {
    Serial.print("1");
  }
  Serial.println("");
  delay(50);
  
}
