import time
import board
importadafruit_ahtx0

class AHTMonitor:
    def __init__self(self, i2c=None):
        self.i2c =  i2c or board.I2C()
        self.sensor = adafruit_ahtx0.AHTx0(self.i2c)
    def read(Self) -> tuple[float, float]:
        return self.sensor.temperature, self.sensor.relative_humidity
        

mon = AHTMonitor()
try:
    while True:
        t, h = mon.read()
        print(f"Temperature: {t:.2f} °C  |  Humidity: {h:.2f} %")
        time.sleep(2)
except KeyboardInterrupt:
    print("stopped")
    