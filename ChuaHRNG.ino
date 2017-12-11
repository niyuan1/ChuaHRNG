// ChuaHRNG.ino
// Read in a digitized double scroll observable as 1 or 0
// sampling at much slower rate than lyapunov timescale
// arduino ChuaHRNG.ino --verify
// arduino ChuaHRNG.ino --upload
// sudo picocom /dev/ttyACM0 -b 9600 -r -l > randbin.txt
// cat randbin.txt | wc -l
// /home/chrisni/Dropbox/Academic/3University2/Phy405/Final/ChuaHRNG

#include <math.h>

int inPin = 2;  // Digital input pin for sampling Chua state voltage
int outPin = 13; // Digital output pin for indicator light

void setup() {
    Serial.begin(9600); // this number is the baud rate (9600 by default)
    pinMode(inPin, INPUT);
    pinMode(outPin, OUTPUT);
}

void loop() {
    int V0;            // Integer value of voltage reading (0/1)
    int V1;            // Second reading for Neuman's trick

    V0 = digitalRead(inPin);
    delay(20);
    V1 = digitalRead(inPin);
    delay(20);

    if (V1 != V0){
      if (V0 == HIGH){
        digitalWrite(outPin, HIGH);
      }
      else {
      digitalWrite(outPin, LOW);
      }
      Serial.println(V0);
    }
}
