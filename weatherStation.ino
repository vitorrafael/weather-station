#include <dht.h>

dht DHT;
void printWeatherData();

// Declares the DHT11 and LDR pin, and the data collect interval.
const int DHT11_PIN = 7;
const int LDR_PIN = A0;
const int DATA_COLLECT_INTERVAL = 360000; // 6 minutes.

void setup(){
  Serial.begin(9600);
}

void loop()
{
  // Reads the DHT11 and the LDR values
  int chk = DHT.read11(DHT11_PIN);
  int ldrValue = analogRead(LDR_PIN);
  // Initializes an array that contains every weather value
  int weatherData[] = {DHT.temperature, DHT.humidity, ldrValue};
  // Calls the printWeatherData function.
  printWeatherData(weatherData);
  // Rest until the next data collect.
  delay(DATA_COLLECT_INTERVAL);
}

void printWeatherData (int weatherDataArray []) {
  // Prints the weather data to the Serial Monitor.
  for (int i = 0; i < 3; i++) {
    // If it's the last item, insert a break line.
    if (i == 2) { 
      Serial.println(weatherDataArray[i]);
    } else {
      Serial.print(weatherDataArray[i]);
      Serial.print(";");
    }
}
