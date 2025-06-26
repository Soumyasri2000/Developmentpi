import pytest
import LDR_Filter
import RPi.GPIO as GPIO
import time


class DummyGPIO:
    def __init__(Self, steps_before_high):
        self.steps = steps_before_high
        self.setup_pin = None
        self.output_val = None
        self.input_calls = 0
    def setup(Self, pin, mode):
        self.setup_pin = mode
    def output(Self, pin, val):
        self.output_val = val
    def input(Self, pin):
        self.input_calls +=1
        return GPIO.LOW if self.input_calls <= self.steps else GPIO.HIGH
    def setmode(self, mode):
        pass
@pytest.fixture(autouse = True)
def patch_sleep(monkeypatch):
    monkeypatch.setattr(time, 'sleep', lambda s : None)
def test_rc_time_counts_steps(monkeypatch, patch_gpio):
    patch_gppio.steps = 5  # 5 retries GPIO will be HIGH
    sensor = LDR_Filter.LDRFilterSensor(pin =)
    count = sensor.rc_time()
    assert count == 5
def test_filter_detected(monkeypatch,patch_gpio):
    patch_gpio.steps = 1500
    sensor = LDR_Filter.LDRFilterSensor(pin=,threshold = 1000)
    assert sensor.filter_present() # count 1500 threshold
def test_filter_not_detected(monkeypatch, patch_gpio):
    patch_gpio = 500
    sensor = LDR_Filter.LDRFilterSensor(pin=,threshold = 1000)
    assert not sensor.filter_present()
    
    
    
    
    
        
        