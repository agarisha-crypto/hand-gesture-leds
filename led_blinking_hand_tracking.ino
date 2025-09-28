int leds[] = {2, 3, 4, 5, 6}; // LED pins
int numLeds = 5;
int num = 0;

void setup() {
  for (int i = 0; i < numLeds; i++) {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    num = Serial.read() - '0'; // number of fingers
    for (int i = 0; i < numLeds; i++) {
      if (i < num) {
        digitalWrite(leds[i], HIGH); // Turn ON LEDs up to num
      } else {
        digitalWrite(leds[i], LOW);  // Others OFF
      }
    }
  }
}
