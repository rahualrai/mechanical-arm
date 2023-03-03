#include <Servo.h>  

// Define servo objects
Servo wrist; // servo 6 on the schematic
Servo three;
Servo two;

// Define variables
int a = 30;

void setup() {
  // Attach servo objects and set initial positions
  three.attach(9);
  two.attach(8);
  wrist.attach(13);
  delay(50);
  three.write(95);
  two.write(2);
  wrist.write(45);
  delay(1000);
}

void loop() {
  // Sweep wrist servo back and forth
  for (int i = 90-a; i <= 90+a; i++) {
    wrist.write(i);
    delay(5);
  }
  for (int i = 90+a; i >= 90-a; i--) {
    wrist.write(i);
    delay(5);
  }
}
