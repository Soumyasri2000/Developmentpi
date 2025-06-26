import serial
import time

class GSMMonitor:
    def __init__(self, port: str = '/dev/ttyS0', baudrate: int = 115200, timeout: float = 1.0):
        self.ser = serial.Serial(port,baudrate=baudrate, timeout=timeout)
        
    def send_At(Self, cmd: str, expect: str = 'OK', timeout: float = 2.0) -> str:
        self.ser.write((cmd+ '\r').encode())
        time.sleep(timeout)
        return self.ser.read_all().decode()
    def check_network(Self) -> bool:
        resp = self.send_at('AT+CREG?', '+CREG:')
        return '+CREG: 0, 1' in resp or '+CREG: 0,5' in resp
    def get_signal(self) -> int:
        resp = self.send_at('AT+CSQ', '+CSQ:')
        parts = resp.split(':',1)[1].strip().split(',')
        return int(parts[0])
    def send_Sms(Self, number: str, msg: str) -> bool:
        self.send_at('AT+CMGF=1', 'OK')
        self.send_at(f'AT+CMGS="{number}"', '>')
        self.ser.write((msg + '\x1A').encode())
        time.sleep(5)
        resp = self.ser.read_all().decode()
        return 'OK' in resp