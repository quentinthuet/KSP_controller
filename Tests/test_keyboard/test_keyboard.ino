//Keyboard report buffer
uint8_t buf[8] = { 0 };   


//Initialisation
void setup() 
{
  Serial.begin(9600);
  randomSeed(analogRead(0));
  delay(200);
}


//programme principale
void loop() 
{
  int randomChar = random(4, 130);
  long randomDelay = random(1000, 10000);

  delay(randomDelay);     // Délais aléatoire
  buf[2] = randomChar;    // Touche aléatoire
  Serial.write(buf, 8);   // Appuis sur la touche
  releaseKey();           // Relache la touche 
}


//Relache d'une touche
void releaseKey() 
{
  buf[0] = 0; buf[2] = 0;
  Serial.write(buf, 8); // signale que l'on relache la touche  
}
