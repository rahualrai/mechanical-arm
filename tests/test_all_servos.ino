#include <Servo.h>

Servo testServo;

void setup() {
  for (int i = 8; i <= 13; i++){
    testServo.attach(i);
    delay(1000);
    testServo.write(40);
    delay(1000);
    testServo.write(90);
    delay(1000);
    testServo.detach();
  }
}


void loop() {
  // put your main code here, to run repeatedly:
}
