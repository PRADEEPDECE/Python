# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:32:49 2023

@author: prade
"""

class Temp_Celsius:
    def __init__(self,temperature=0):
        print("Assigning temperature value")
        self._temperature=temperature
    def convert_to_fahrenheit(self):
        return (self._temperature*1.8)+32
    @property
    def temperature(self):
        print("Getting temperature value")  
        return self._temperature
    @temperature.setter
    def temperature(self,value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting temperature value")
        self._temperature=value
    #temperature=property()
   # temperature=temperature.getter(get_temperature)
    #temperature=temperature.setter(set_temperature)
c=Temp_Celsius(10)
print(c.temperature)
c.temperature=100
print(c.temperature)
