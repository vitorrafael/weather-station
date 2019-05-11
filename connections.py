""" Classes that represents the communications between the arduino, computer
    and the ThingSpeak. """

import os
from socket import gaierror
import urllib.request
from urllib.error import URLError
import serial



API_KEY = os.getenv("API_KEY")
URL = "https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}"


def test_internet_connection():
    """ Tests the internet connection. """
    try:
        urllib.request.urlopen("https://www.google.com/", timeout=10)
    except:
        raise InternetConnectionError


def send_data_to_server(temperature, humidity, light_incidence):
    """ Sends the data to the ThingSpeak server. """
    try:
        urllib.request.urlopen(URL.format(API_KEY, temperature,
                                          humidity, light_incidence))
    except (URLError, gaierror) as e:
        print(str(e))
        raise InternetConnectionError


class SerialConnection():
    """ Represents the USB Serial connection between the
    Arduino and the computer. """

    def __init__(self):
        self.arduino_port = os.getenv("PORT")
        self.arduino = None

    def start_connection(self):
        """ Starts the connection between the Arduino
        and the computer through the USB serial. """
        try:
            self.arduino = serial.Serial(self.arduino_port, 9600, timeout=1)
        except (serial.SerialException) as e:
            print(str(e))
            return False
        return True

    def get_arduino_data(self):
        """ Fetchs the arduino data sended through the USB serial. """
        return self.arduino.readline().decode("utf-8")


class InternetConnectionError(Exception):
    """ Exception to be raised when a problem in the
    internet connection is detected. """

    def __init__(self):
        self.msg = "There's a problem in the internet connection"
        super().__init__(self.msg)
