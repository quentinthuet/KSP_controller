///////////////////////////////////////////////////////////////////////////////
//                          @author: Quentin Thuet                           //
//                         @project: KSP controller                          //
//                          @file: KSP_controller                            //
//                      @description: Arduino MEGA code                      //
///////////////////////////////////////////////////////////////////////////////

   //////////////////////
   // GLOBAL VARIABLES //
   //////////////////////

// Digital pins //

  // Push
int seq_pin = 12;

  // Switches
int action_group_pin[10] = {2,3,4,5,6,7,8,9,10,11};
int rcs_pin = 22, sas_pin = 24, lights_pin = 26, gears_pin = 28, brakes_pin = 30, solar_panels_pin = 32, antennas_pin = 34, thrust_reversers_pin = 36,
abort_pin = 38, rotation_joystick_activation_pin = 40, translation_joystick_activation_pin = 42, staging_activation_pin = 44, camera_activation_pin = 46;
  
  // Leds
int rcs_led = 23, sas_led = 25, lights_led = 27, gears_led = 29, brakes_led = 31, solar_panels_led = 33, antennas_led = 35, thrust_reversers_led = 37,
abort_led = 39;

// Analog pins //

int pitch_pin = 0, yaw_pin = 1, roll_pin = 2, x_translation_pin = 3, y_translation_pin = 4, z_translation_pin = 5, throttle_pin = 6, zoom_pin = 7,
x_camera_pin = 8, y_camera_pin = 9; 

// Boolean variables //

int rcs = 0, sas = 0, lights = 0, gears = 0, brakes = 0, solar_panels = 0, antennas = 0, thrust_reversers = 0, abort_on = 0;



   ///////////
   // SETUP //
   ///////////

void setup() {

  // Pin assignment //

   // Switches
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
  pinMode(sas_pin, INPUT_PULLUP);
  pinMode(lights_pin, INPUT_PULLUP);
  pinMode(gears_pin, INPUT_PULLUP);
  pinMode(brakes_pin, INPUT_PULLUP);
  pinMode(solar_panels_pin, INPUT_PULLUP);
  pinMode(antennas_pin, INPUT_PULLUP);
  pinMode(thrust_reversers_pin, INPUT_PULLUP);
  pinMode(abort_pin, INPUT_PULLUP); 
  pinMode(rotation_joystick_activation_pin, INPUT_PULLUP);
  pinMode(translation_joystick_activation_pin, INPUT_PULLUP);
  pinMode(staging_activation_pin, INPUT_PULLUP);
  pinMode(camera_activation_pin, INPUT_PULLUP);

   // Leds
  pinMode(rcs_led, OUTPUT);
  pinMode(sas_led, OUTPUT);
  pinMode(lights_led, OUTPUT);  
  pinMode(gears_led, OUTPUT);
  pinMode(brakes_led, OUTPUT);
  pinMode(solar_panels_led, OUTPUT);
  pinMode(antennas_led, OUTPUT);
  pinMode(thrust_reversers_led, OUTPUT); 
  pinMode(abort_led, OUTPUT);
  Serial.begin(9600);
}



   //////////
   // LOOP //
   //////////

void loop() {

  // Pin reading and serial writing //

   // Digital pins
  Serial.println(String(digitalRead(action_group_pin[0]))
    +String(digitalRead(action_group_pin[1]))
    +String(digitalRead(action_group_pin[2]))
    +String(digitalRead(action_group_pin[3]))
    +String(digitalRead(action_group_pin[4]))
    +String(digitalRead(action_group_pin[5]))
    +String(digitalRead(action_group_pin[6]))
    +String(digitalRead(action_group_pin[7]))
    +String(digitalRead(action_group_pin[8]))
    +String(digitalRead(action_group_pin[9]))
    +String(digitalRead(seq_pin))
    +String(digitalRead(rcs_pin))
    +String(digitalRead(sas_pin))
    +String(digitalRead(lights_pin))
    +String(digitalRead(gears_pin))
    +String(digitalRead(brakes_pin))
    +String(digitalRead(solar_panels_pin))
    +String(digitalRead(antennas_pin))
    +String(digitalRead(thrust_reversers_pin))
    +String(digitalRead(abort_pin))
    +String(digitalRead(rotation_joystick_activation_pin))
    +String(digitalRead(translation_joystick_activation_pin))
    +String(digitalRead(staging_activation_pin))
    +String(digitalRead(camera_activation_pin)));

   // Analog pins
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


  // Serial reading  //
  
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
    abort_on = Serial.parseInt();
    Serial.read();

    // Pins writing //
    
    digitalWrite(rcs_led, rcs); 
    digitalWrite(sas_led, sas);   
    digitalWrite(lights_led, lights);
    digitalWrite(gears_led, gears);  
    digitalWrite(brakes_led, brakes);  
    digitalWrite(solar_panels_led, solar_panels);  
    digitalWrite(antennas_led, antennas);  
    digitalWrite(thrust_reversers_led, thrust_reversers);    
    digitalWrite(abort_led, abort_on);
  }
}
