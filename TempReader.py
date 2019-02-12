#!/usr/bin/env python3

import os
import glob
import time

# -----------------------------------------------------
# Code borrowed from http://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/
class TempReader:
    def __init__(self):
      os.system('modprobe w1-gpio')
      os.system('modprobe w1-therm')
      
      # Find path to sensor
      base_dir = '/sys/bus/w1/devices/'
      device_folder = glob.glob(base_dir + '28*')[0]
      self.device_file = device_folder + '/w1_slave'

    # Read raw data
    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    # Read temperature in celcius
    def read_temp(self):
        lines = read_temp_raw()
        
        # Wait for reading
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        
        # Find temperature position
        equals_pos = lines[1].find('t=')
        
        temp_c = 126000 # default return max temp + 1deg celcius
        # If temperature reading found. Pick it and convert to celcius
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
        
        # Return temperature in celcius
        return temp_c
	
