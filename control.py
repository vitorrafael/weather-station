""" Controls the software process """

from time import sleep
import connections as cnt


# Creates the arduino connection object
ARDUINO_CONNECTION = cnt.SerialConnection()

# Tests the internet connection
cnt.test_internet_connection()

# Starts the arduino connection
CONNECTED_TO_ARDUINO = ARDUINO_CONNECTION.start_connection()

while CONNECTED_TO_ARDUINO:
    BRUTE_DATA = ARDUINO_CONNECTION.get_arduino_data()
    if BRUTE_DATA:
        DATA = BRUTE_DATA.split(";")
        # Separates the brute data into three variables
        TEMPERATURE = DATA[0]
        HUMIDITY = DATA[1]
        LIGHT_INCIDENCE = DATA[2]

        # Sends the data to the server
        cnt.send_data_to_server(TEMPERATURE, HUMIDITY, LIGHT_INCIDENCE)

        # Prints the data
        print("Temperature: {}\n Humidity: {}\n Light Incidence: {}\n".format(
            TEMPERATURE, HUMIDITY, LIGHT_INCIDENCE))

        # Sleeps for two seconds
        sleep(2)
