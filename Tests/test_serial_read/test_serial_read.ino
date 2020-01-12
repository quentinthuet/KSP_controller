
void setup()
{
  pinMode(7, OUTPUT);
  pinMode(8,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
    while(Serial.available()) {
         int lu = Serial.parseInt();
        flash(7,lu);
        Serial.read();
        lu = Serial.parseInt();
        flash(8,lu);
    }
    delay(1000);
}

void flash(int pin,int n)
{
  for (int i = 0; i < n; i++)
  {
    digitalWrite(pin, HIGH);
    delay(1000);
    digitalWrite(pin, LOW);
    delay(1000);
  }
}
