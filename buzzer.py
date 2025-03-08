from machine import Pin, PWM
import time
import gc
try:
    # Hardware setup
    BUZZER_PIN = 0  # D3 = GPIO0
    buzzer = PWM(Pin(BUZZER_PIN))
    buzzer.duty(0)  # Start with buzzer off

    # Simple tone control function
    def play_tone(freq=1000, duration=900):
        buzzer.freq(freq)
        buzzer.duty(512)  # 50% duty cycle
        time.sleep_ms(duration)
        buzzer.duty(0)

    # Main loop with demo pattern
    while True:
        # Example: Beep every 2 seconds
        play_tone(1000, 900)  # 1000Hz for 900ms
        time.sleep(2)
        gc.collect()
except Exception as e:
    print("Error:", e)
    machine.reset()  # Optional: Force reset after error
