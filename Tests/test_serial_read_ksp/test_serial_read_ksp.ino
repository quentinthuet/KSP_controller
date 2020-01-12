int rcs;
int sas;
void setup() {
  // put your setup code here, to run once:
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}

void loop() {
    while(Serial.available()) {
         rcs = Serial.parseInt();
         Serial.read();
         sas = Serial.parseInt();
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
    }
}
