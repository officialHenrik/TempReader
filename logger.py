#!/usr/bin/env python3

import time
import schedule
from influxdb import InfluxDBClient
from TempReader import TempReader

from datetime import datetime

# ------------------------------------------------------
# Influx cfg
USER = 'root'
PASSWORD = 'root'
DBNAME = 'test'
HOST = '192.168.0.110'
PORT = 8086

points = []

# ------------------------------------------------------
def get_point():

    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    t = TempReader().read_temp() # Get current temperature
    point = {
        "measurement": 'Temp',
        "time": current_time,
        "tags": {
            "location": 'Eklanda_living_room',
            "sensor": "DS18B20"
        },
        "fields": {
             "temp": t
                }
            }
    return(point)

# ------------------------------------------------------
# Callback for writing data to database
def log_to_db():
    global points
    # Insert into db
    p1 = get_point()
    points.append(p1)
    try:
        client = InfluxDBClient(HOST, PORT, USER, PASSWORD, DBNAME)
        if(client.write_points(points)):
            print(points)
            points = []
        else:
            print("Warning: failed inserting into influxdb")
    except:
        print("Influx connection failed.")

# ------------------------------------------------------
# Schedule logging
schedule.every(5).minutes.do(log_to_db)

# Run forever
try:
    schedule.run_all()
    while True:
       	schedule.run_pending()
        time.sleep(1)
finally:
    print("temp logger failed...")
