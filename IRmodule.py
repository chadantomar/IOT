#IR Sensor : Calculate Number of Object passed 
from machine import ADC, Pin
import time

# Initialize hardware
sensor = ADC(0)  # A0 pin on ESP8266
count = 0

while True:
    # Read sensor value (0-1024)
    ir_value = sensor.read()
    print("Sensor value:", ir_value)
    
    # Check threshold and increment counter
    if ir_value < 600:
        count += 1
        print("Count:", count)
    
    # Wait 1 second between readings
    time.sleep(1)
