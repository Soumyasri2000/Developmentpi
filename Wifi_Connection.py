import subprocess
import re

class WifiMonitor:
    def __init__(Self, interface='wlan0', ssid=None, password=None):
        self.interface = interface
        self.ssid = ssid
        self.password = paswword
    def connect(Self) -> bool:
        if not self.ssid or not self.password:
            raise ValueError("SSID and Password must be provided")
        cmd = ['iwconfig', self.interface, 'essid', self.ssid, 'key', self.password]
        try:
            subprocess.check_output(cmd, text = True)
            return True
        except subprocess.CalledProcessError:
            return false
    def get_signal_dbm(Self) -> int:
        out = subprocess.check_output((['iwconfig', self.interface], text=True)
        m = re.search(r'Signal level=([-\d]+) dBm', out)
        if not m:
            raise ValueError("Signal level not found")
        return int(m.group(1))
        