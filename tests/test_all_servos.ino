#include <Servo.h>

Servo servoZX1;

int unknownServo1 = 8;
int unknownServo2 = 9;
int unknownServo3= 10;
int unknownServo4 = 11;
int unknownServo5 = 12;
int unknownServo6 = 13;




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
