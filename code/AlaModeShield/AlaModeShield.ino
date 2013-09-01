
#include <LiquidCrystal.h>

// pins for Freetronics LCD Shield

LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

void setup() 
{
  lcd.begin(16, 2);
  lcd.print("Counting!");
}

void loop() 
{
  lcd.setCursor(0, 1);
  lcd.print(millis() / s1000);
}

