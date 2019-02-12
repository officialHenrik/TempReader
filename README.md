# TempReader
reads temperature from a DS18B20 temperature sensor

## Enable the onw wire interface

1. Add to boot

        sudo nano /boot/config.txt, 
    add:
        dtoverlay=w1–gpio

2. sudo reboot

3. Enable kernel modules

        sudo modprobe w1–gpio
        sudo modprobe w1-therm
