#include <Stepper.h>

const int stepsPerRevolution = 200;
int x;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();
  if (x == 1) {
    Serial.print("forward");
  }
  if (x == 2) {
  Serial.print("back");
  }
  if (x == 3) {
  Serial.print("up");
  }
  if (x == 4) {
  Serial.print("down");
  }
}
