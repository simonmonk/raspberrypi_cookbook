// ArduinoHello

void setup()
{
  Serial.begin(9600); 
}

void loop()
{
  Serial.println("Hello Raspberry Pi");
  delay(1000);
}
