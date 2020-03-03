#include <Servo.h>
int pin_open = 10;  // 定义针脚号，数字类型为整型
void setup() {
  pinMode(pin_open, OUTPUT);
}
void loop() {
  digitalWrite(pin_open, HIGH);
  delay(1000);
  digitalWrite(pin_open, LOW);
  delay(1000);

}
