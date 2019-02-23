# TempReader
reads temperature from a DS18B20 temperature sensor

## Enable the onw wire interface

1. Open boot config

        sudo nano /boot/config.txt, 
2. Add to bottom

        dtoverlay=w1–gpio

3. Reboot the pi

4. Enable kernel modules

        sudo modprobe w1-gpio
        sudo modprobe w1-therm

5. Test

        cd /sys/bus/w1/devices
        cd 28-xxxx
        cat w1_slave
