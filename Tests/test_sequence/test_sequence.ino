int data = 0;
int altitude = 0;

void setup(){
  Serial.begin(9600);//initialisation port série
  pinMode(2,INPUT_PULLUP);//pin n°7 en entrée (bouton)
  pinMode(3,INPUT_PULLUP);//pin n°7 en entrée (bouton)
  pinMode(4,INPUT_PULLUP);//pin n°7 en entrée (bouton)
  pinMode(5,INPUT_PULLUP);//pin n°7 en entrée (bouton)
  pinMode(6,INPUT_PULLUP);//pin n°7 en entrée (bouton)
  pinMode(7,OUTPUT);//pin n°7 en entrée (bouton)
  pinMode(8,OUTPUT);//pin n°7 en entrée (bouton)
  pinMode(9,OUTPUT);//pin n°7 en entrée (bouton)
  pinMode(10,OUTPUT);//pin n°7 en entrée (bouton)
  digitalWrite(7,1);
  digitalWrite(8,1);
  digitalWrite(9,1);
  digitalWrite(10,1);
}

//à chaque boucle
void loop(){

  if (Serial.available() > 0) {
      //récup de l’altitude transmise
    data = Serial.parseInt();//séparateur
    if (data == 1){
      digitalWrite(7,0);
    }
    else if (data == 0){
      digitalWrite(7,1);
    }
    digitalWrite(8,1);
  }
  else {
    digitalWrite(8,0);
  }
  if(digitalRead(2) == 0){//si l’état du bouton est différent de précédemment
  
    Serial.println("seq");//on envoie le message « boutST » au port série
    delay(100);//délai de 100ms par sécurité
  }
  if (digitalRead(3) == 0){

    Serial.println("rcs");
    delay(100);
  }
  if (digitalRead(4) == 0){
    Serial.println("sas");
    delay(100);
  }
  if (digitalRead(5) == 0){
    Serial.println("abort");
    delay(100);
  }
  if (digitalRead(6) == 0){
    Serial.println("solar_panels");
    delay(100);
  }
  delay(100); 
}
