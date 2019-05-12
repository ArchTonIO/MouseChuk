/*Code to upload into Arduino, rename it Main.ino if you're going to use arduino ide
Antonio Del Cogliano, 04/05/2019*/
#include <Arduino.h>//only needed if you are NOT using the arduino ide
#include <Wire.h>
#include <nunchuk.h>
int x = 0;
int y = 0;
void setup() {
    Serial.begin(9600);
    Wire.begin();
    nunchuk_init();
}
int angle = 0;
void mapValues(){
    angle = Angle();
    if ((nunchuk_joystickX_raw()==128 || nunchuk_joystickX_raw()==127) && nunchuk_joystickY_raw()==126){
        angle = 0;

    }
    x = map(nunchuk_joystickX(), -102, 103, 0, 20);
    y = map(nunchuk_joystickY(), -103, 98, 0, 20);
    if(nunchuk_buttonC() == 1){
      x = 547;
      delay(100);

    }
    if (nunchuk_buttonZ() == 1){
      y = 896;
      delay(100);

    }
    if(nunchuk_accelY()>=100){
        x = 354;
        delay(100);
    }
    if(nunchuk_accelY()<= -100){
        y = 657;
        delay(100);
    }

}
void printAllData(){
  mapValues();
  Serial.print("Asse x: ");
  Serial.print(x, DEC);
  Serial.print("||");
  Serial.print("Asse y: ");
  Serial.print(y, DEC);
  Serial.print("||");
  nunchuk_printC();
  Serial.print("||");
  nunchuk_printZ();
  Serial.print("||");
  nunchuk_printAngle();
  Serial.print("||");
  Serial.print(SlidingSpeed());
  Serial.print("||");
  Serial.print(angle);
  Serial.print("||");
  Serial.print(nunchuk_joystickX_raw());
  Serial.print("||");
  Serial.print(nunchuk_joystickY_raw());
  Serial.print("||");
  Serial.print(nunchuk_accelY());
  Serial.print("\n");
  delay(500);
}

void toSerial(){
  mapValues();
  Serial.println(x);
  delay(1);
  Serial.println(y);
  delay(1);

}

void loop() {
  if (nunchuk_read()) {
    //printAllData();
    toSerial();
  }
}
