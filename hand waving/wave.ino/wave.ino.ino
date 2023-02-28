#include <Servo.h>  

// Define servo objects
Servo wrist;
Servo two;
Servo one;

// Define variables
int a = 30;

void setup() {
  // Attach servo objects and set initial positions
  two.attach(9);
  one.attach(8);
  wrist.attach(13);
  delay(50);
  two.write(95);
  one.write(2);
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
