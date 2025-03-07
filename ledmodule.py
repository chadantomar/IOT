from machine import Pin
import time

# Internal LED (GPIO2, active-low on NodeMCU)
led_internal = Pin(2, Pin.OUT)

# External LED (GPIO5 / D1)
led_external = Pin(5, Pin.OUT)

while True:
    # Turn ON both LEDs
    led_internal.on()   # Internal LED (active-low: ON = LOW)
    led_external.on()   # External LED (ON = HIGH)
    print("LEDs ON")
    time.sleep(1)

    # Turn OFF both LEDs
    led_internal.off()  # Internal LED (active-low: OFF = HIGH)
    led_external.off()  # External LED (OFF = LOW)
    print("LEDs OFF")
    time.sleep(1)
