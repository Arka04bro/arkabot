#include <Servo.h> // подключаем библиотеку для работы с сервоприводом

Servo servo1; // объявляем переменную servo типа "servo1"

void setup() {
   servo1.attach(8); // привязываем сервопривод к аналоговому выходу 11
}
void loop() {
   servo1.write(0); // ставим угол поворота под 0
   delay(2000); // ждем 2 секунды
   servo1.write(90); // ставим угол поворота под 90
   delay(2000); // ждем 2 секунды
}
