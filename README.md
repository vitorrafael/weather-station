# Weather Station

## Objective:
   - Collect data from the environment using an Arduino
   - Send these data to an Internet of Things platform using Python
   - Plot graphs about each information

## Instructions:
### Before the code:
   You'll have to create an account in [Thing Speak](https://thingspeak.com/). <br>
   After that, create a channel with three fields, each one will have an different information.

### Setting up the Arduino:
   To set up the Arduino, just follow these tutorial:
   - [DHT11 Sensor](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-an-arduino/)
   - [Light Dependent Resistor-LDR](https://maker.pro/arduino/tutorial/how-to-use-an-ldr-sensor-with-arduino)<br>
   **If you use _any_ input different from the code, remember to change which input the Arduino will read in the .ino file.**

### The Python Code:
   Change the empty variables to your values:
   - The **API_KEY** can be found in the Thing Speak channel.
   - In the **ARDUINO_PORT** you must insert which USB port the Arduino is connected.<br>

### Visualizing the Graphs:
   Now the three graphs should be visible in your Thing Speak channel.
