# coding: utf-8
import random

from sense_hat import SenseHat


class SenseHatDataFetcher:
    def __init__(self):
        pass

    def read_temperature(self):
        sense = SenseHat()
        temp = sense.get_temperature()
        return temp

    
    def read_humidity(self):
        sense = SenseHat()
        humidity = sense.get_humidity()
        return humidity

    def read_pressure(self):
        sense = SenseHat()
        pressure = sense.get_pressure()
        return pressure

    