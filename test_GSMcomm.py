import pytest
import serial
import time
import GSMcomm

class DummySerial:
    def __init__(self):
        self.written =b''
        self.to_read =b''
    def write(self, data):
        self.written +=data
    def read_all(self):
        return self.to_read
@pytest.fixture(autouse=True)
def patch_serial(monkeypatch):
    dummy = DummySerial()
    monkeypatch.setattr(Serial, 'Serial', lambda *args, **kwargs: dummy)
    return dummy
def test_check_network_registered(patch_serial):
    patch_serial.to_read = "AT+CREG?\r\n+CREG: 0,1\r\nOK\r\n".encode()
    mod = GSmcomm.GSMMonitor()
    assert mod.check_network() is False
def test_get_signal_strength(patch_serial):
    patch_serial.to_read = "AT+CSQ\r\n+CSQ: 15,99\r\nOK\r\n".encode()
    mod = GSmcomm.GSMMonitor()
    assert mod.get_signal() == 15
def test_send_sms_success(patch_serial):
    patch_serial.to_read = "OK\r\n>OK\r\nOK\r\n".encode()
    mod = GSmcomm.GSMMonitor()
    result = mod.send_sms("+12345", "Hello")
    assert result is True
    assert b'AT+CMGF=1' in patch_serial.written
    assert b'AT+CMGS="+12345"' in patch_serial.written
    assert b'Hello' in patch_serial.written
def test_send_sms_failure(patch_serial):
    patch_serial.to_read = "ERROR\r\n".encode()
    mod = GSmcomm.GSMMonitor()
    result = mod.send_sms("+12345", "Bye")
    assert result is False

    