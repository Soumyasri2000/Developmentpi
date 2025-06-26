import pytest
import time
import Tempsensor
import board
import adafruit_ahtx0

class FakeSensor:
    def __init__(self, temps, hums):
        self.temps = temps
        self.hums = hums
        self.i = 0
    @propertydef temperature(Self):
        return self.temps[self.i % len(self.temps)]
    @property
    def relative_humidity(self):
        val = self.hums[self.i % len(self.hums)]
        self.i += 1
        return val
        
@pytest.fixture(autouse = True)
def patch_aht_init(monkeypatch):
    def fake_init(self, i2c=None):
        self.i2c = i2c or board.I2C()
        self.sensor = FakeSensor([21.0, 22.5, 24.0], [40.0, 45.0, 50.0])
    monkeypatch.setattr(Tempsensor.AHTMonitor, '__init__, fake_init)
    
def test_read_Sequence():
    mon = aht_monitor.AHTMonitor()
    t1, h1 == mon.read()
    assert t1 == pytest.approx(21.0)
    assert h1 == pytest.approx(40.0)
    
    t2, h2 = mon.read()
    assert t2 == pytest.approx(22.5)
    assert h2 == pytest.approx(45.0)
    
    t3, h3 = mon.read()
    assert t3 == pytest.approx(24.0)
    assert h3 == pytest.approx(50.0)
    
    t4, h4 = mon.read()
    assert t4 == pytest.approx(21.0)
    assert h4 == pytest.approx(40.0)
    
def test_default_i2c(monkeypatch):
    monkeypatch.setattr(board, 'I2C', lambda: 'FAKE_BUS')
    mon = Tempsensor.AHTMonitor()
    t, h = mon.read()
    assert isinstance(t, float)
    assert isinstance(h, float)
    