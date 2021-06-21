#include <Stepper.h>

const int stepsPerRevolution = 200;
int x;

Stepper a_Stepper(stepsPerRevolution, 8, 9, 10, 11);
Stepper b_Stepper(stepsPerRevolution, 4, 5, 6, 7);

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  a_Stepper.setSpeed(30);
  b_Stepper.setSpeed(30);
}

void loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();
  if (x == 1) {
    Serial.print("forward");
    a_Stepper.step(stepsPerRevolution/4);
  }
  if (x == 2) {
  Serial.print("back");
  a_Stepper.step(-stepsPerRevolution/4);
  }
  if (x == 3) {
  Serial.print("up");
  b_Stepper.step(stepsPerRevolution);
  }
  if (x == 4) {
  Serial.print("down");
  b_Stepper.step(-stepsPerRevolution);
  }
}
