# Weather Station

## Objective:
    * Collect data from the environment using an Arduino
    * Send these data to an Internet of Things platform using Python
    * Plot graphs about each information

### Before the code:
    You'll have to create an account in the Thing Speak.
    https://thingspeak.com/
    [ThingSpeak](https://thingspeak.com/)
    After that, create a channel with three fields, each one will have an different information.

### Setting up the Arduino:
    To set up the Arduino, just follow these tutorial:
        * http://www.circuitbasics.com/how-to-set-up-the-dht11
         [CircuitBasis](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-an-arduino/)
        * https://maker.pro/arduino/tutorial/how-to-use-an-ldr-sensor-with-arduino
         [Maker](https://maker.pro/arduino/tutorial/how-to-use-an-ldr-sensor-with-arduino)
   ** If you use any input different from the code, remember to change which analog the Arduino will read in the .ino file. **

### The Python Code:
    Change the empty variables to your values:
        * The API_KEY can be found in the Thing Speak channel.
        * In the ARDUINO_PORT you must insert which USB port the Arduino is connected.

### Visualizing the Graphs:
    Now the three graps should be plotted in your Thing Speak channel.
