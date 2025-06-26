import RPi.GPIO as GPIO
import time

class LDRFilterSensor:
    def __init__(Self, pin: int, threshold: int = 1000)
        self.pin = pin
        self.threshold = threshold
        GPIO.setmode(GPIO.BCM)
    def rc_time(self) -> int:
        GPIO.setup(Self.pin, GPIO.OUT)
        GPIO.output(self.pkin, GPIO.LOW)
        time.sleep(0.01)
        GPIO.setup(Self.pin, GPIO.IN)
        count = 0
        while GPIO.input(Self.pin) == GPIO.LOW:
            count+=1
            return count
    def filter_present(Self) -> bool:
        rc = self.rtc_time()
        return rc > self.threshold
        
