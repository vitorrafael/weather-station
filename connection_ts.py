""" 
    Creates the communication between the Arduino weather values and the ThingSpeak
    channel, were they will be visible in graphs
"""

import os
import urllib.request
from urllib.error import URLError
from socket import gaierror
from serial import Serial

ARDUINO_PORT = '' # Insert the USB Port which the Arduino is connected
API_KEY = '' # Insert the API from your ThingSpeak channel
URL = 'https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}'

# Grants access to read the Arduino's Serial Monitor
os.system('chmod 666 {}').format(ARDUINO_PORT)
# Connects to the Arduino Serial Monitor
ARDUINO = Serial(ARDUINO_PORT, 9600, timeout=1)

def print_weather_values(weather_list):
    ''' Prints all the weather values collected by the Arduino. '''
    weather_list_length = len(weather_list)
    for i in range(weather_list_length):
        ''' Iterates through the weather values list, printing each
        one of them, and in the last item insert a break line. '''
        if i == (weather_list_length):
            print(weather_list[i])
        else:
            print(weather_list[i], end=";")

while True:
    try:
        SERIAL_MONITOR_VALUES = ARDUINO.readline().decode("utf-8")
        if SERIAL_MONITOR_VALUES:
            weather_values = SERIAL_MONITOR_VALUES.split(';')

            # Assign each value to a different variable
            temperature = weather_values[0]
            humidity = weather_values[1]
            light_presence = weather_values[2]

            # Communicates with Thingspeak channel, sending the data in order to create the graphs
            urllib.request.urlopen(URL.format(API_KEY, temperature, humidity, light_presence))

            # Print the weather values to the terminal, in the following order:
            # TEMPERATURE;HUMIDITY;LIGHT_PRESENCE
            print_weather_values(weather_values)

    except (URLError, gaierror) as error:
        # Connection errors that might stop the execution of the script
        print("Connection Error!")
