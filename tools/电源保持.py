import serial
import logging
import time

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

while True:
    t = serial.Serial('COM3', 9600)
    logging.info("sending...")
    t.write(bytes.fromhex("558899"))
    t.close()
    time.sleep(30)
