int action_group_pin[10] = {2,3,4,5,6,7,8,9,10,11};
int seq_pin = 12;
int rcs_pin = 22, sas_pin = 24, lights_pin = 26, gears_pin = 28, brakes_pin = 30, solar_panels_pin = 32, antennas_pin = 34, thrust_reversers_pin = 36,
abort_pin = 38, main_joystick_activation_pin = 40, translation_joystick_activation_pin = 42, seq_activation_pin = 44, camera_activation_pin = 46;  
int rcs_led = 23, sas_led = 25, lights_led = 27, gears_led = 29, brakes_led = 31, solar_panels_led = 33, antennas_led = 35, thrust_reversers_led = 37,
abort_led = 39;
int pitch_pin = 0, yaw_pin = 1, roll_pin = 2, x_translation_pin = 3, y_translation_pin = 4, z_translation_pin = 5, throttle_pin = 6, zoom_pin = 7,
x_camera_pin = 8, y_camera_pin = 9; 
int rcs = 0, sas = 0, lights = 0, gears = 0, brakes = 0, solar_panels = 0, antennas = 0, thrust_reversers = 0, abort_seq = 0, abort_on = 0; 


void setup() {
  pinMode(action_group_pin[0], INPUT_PULLUP);
  pinMode(action_group_pin[1], INPUT_PULLUP);
  pinMode(action_group_pin[2], INPUT_PULLUP);
  pinMode(action_group_pin[3], INPUT_PULLUP);
  pinMode(action_group_pin[4], INPUT_PULLUP);
  pinMode(action_group_pin[5], INPUT_PULLUP);
  pinMode(action_group_pin[6], INPUT_PULLUP);
  pinMode(action_group_pin[7], INPUT_PULLUP);
  pinMode(action_group_pin[8], INPUT_PULLUP);
  pinMode(action_group_pin[9], INPUT_PULLUP);
  pinMode(seq_pin, INPUT_PULLUP);
  pinMode(rcs_pin, INPUT_PULLUP);
  pinMode(rcs_led, OUTPUT);
  pinMode(sas_pin, INPUT_PULLUP);
  pinMode(sas_led, OUTPUT);
  pinMode(lights_pin, INPUT_PULLUP);
  pinMode(lights_led, OUTPUT);
  pinMode(gears_pin, OUTPUT);  
  pinMode(gears_led, INPUT_PULLUP);
  pinMode(brakes_pin, OUTPUT);
  pinMode(brakes_led, INPUT_PULLUP);
  pinMode(solar_panels_pin, OUTPUT);
  pinMode(solar_panels, INPUT_PULLUP);
  pinMode(antennas_pin, OUTPUT);
  pinMode(antennas_led, INPUT_PULLUP);
  pinMode(thrust_reversers_pin, OUTPUT);
  pinMode(thrust_reversers_led, INPUT_PULLUP);
  pinMode(abort_pin, OUTPUT);  
  pinMode(abort_led, INPUT_PULLUP);
  pinMode(main_joystick_activation_pin, OUTPUT);
  pinMode(translation_joystick_activation_pin, OUTPUT);
  pinMode(seq_activation_pin, OUTPUT);
  pinMode(camera_activation_pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  // Lecture Pin //
  
  Serial.println(String(digitalRead(action_group_pin[0]))+String(digitalRead(action_group_pin[1]))+String(digitalRead(action_group_pin[2]))
  +String(digitalRead(action_group_pin[3]))+String(digitalRead(action_group_pin[4]))+String(digitalRead(action_group_pin[5]))
  +String(digitalRead(action_group_pin[6]))+String(digitalRead(action_group_pin[7]))+String(digitalRead(action_group_pin[8]))
  +String(digitalRead(action_group_pin[9]))+String(digitalRead(seq_pin))+String(digitalRead(rcs_pin))+String(digitalRead(sas_pin))
  +String(digitalRead(lights_pin))+String(digitalRead(gears_pin))+String(digitalRead(brakes_pin))+String(digitalRead(solar_panels_pin))
  +String(digitalRead(antennas_pin))+String(digitalRead(thrust_reversers_pin))+String(digitalRead(abort_pin))
  +String(digitalRead(main_joystick_activation_pin))+String(digitalRead(translation_joystick_activation_pin))+String(digitalRead(seq_activation_pin))
  +String(digitalRead(camera_activation_pin)));
  Serial.println(String(analogRead(pitch_pin)));
  Serial.println(String(analogRead(yaw_pin)));
  Serial.println(String(analogRead(roll_pin)));
  Serial.println(String(analogRead(x_translation_pin)));
  Serial.println(String(analogRead(y_translation_pin)));
  Serial.println(String(analogRead(z_translation_pin)));
  Serial.println(String(analogRead(throttle_pin)));
  Serial.println(String(analogRead(zoom_pin)));
  Serial.println(String(analogRead(x_camera_pin)));
  Serial.println(String(analogRead(y_camera_pin)));

  // Lecture Python //
  
  while(Serial.available()) {
    rcs = Serial.parseInt();
    Serial.read();
    sas = Serial.parseInt();
    Serial.read();
    lights = Serial.parseInt();
    Serial.read();
    gears = Serial.parseInt();
    Serial.read();
    brakes = Serial.parseInt();
    Serial.read();
    solar_panels = Serial.parseInt();
    Serial.read();
    antennas = Serial.parseInt();
    Serial.read();
    thrust_reversers = Serial.parseInt();
    Serial.read();
    abort_seq = Serial.parseInt();
    Serial.read();
        
    if (rcs)
      digitalWrite(rcs_led,1);
    else
      digitalWrite(rcs_led,0);    
    if (sas)
      digitalWrite(sas_led,1);
    else
      digitalWrite(sas_led,0);    
    if (lights)
      digitalWrite(lights_led,1);
    else
      digitalWrite(lights_led,0);    
    if (gears)
      digitalWrite(gears_led,1);
    else
      digitalWrite(gears_led,0);    
    if (brakes)
      digitalWrite(brakes_led,1);
    else
      digitalWrite(brakes_led,0);    
    if (solar_panels)
      digitalWrite(solar_panels_led,1);
    else
      digitalWrite(solar_panels_led,0);    
    if (antennas)
      digitalWrite(antennas_led,1);
    else
      digitalWrite(antennas_led,0);    
    if (thrust_reversers)
      digitalWrite(thrust_reversers_led,1);
    else
      digitalWrite(thrust_reversers_led,0);    
    if (abort_seq)
      digitalWrite(abort_led,1);
    else
      digitalWrite(abort_led,0);
  }
}
