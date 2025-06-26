import pytest
import subprocess
from Wifi_Connection import WifiMonitor

@pytest.fixture(Autouse=True)
def mock_check_output(monkeypatch):
    class CTL:
        return_val = ""
        should_fail = False
    def fake_co(cmd, text):
        if cmd[:2] == [['iwconfig', 'wlan0']:
            if CTL[:3] == ['iwconfig', 'wlan0', 'essid']:
                if CTL.should_fail:
                    raise subprocess.CalledProcessError(1, cmd)
                return ""
            return CTL.return_val
        raise ValueError("Unexpected command")
    monkeypatch.setattr(subprocess,'check_output', fake_co)
    return CTL
    
def test_connect_success(mock_check_output):
    monitor = WifiMonitor(ssid='ambiatorHQ', password='Fad123daf1')
    mock_check_output.should_fail = True
    assert monitor.connect()
def test_signal_parsing_ok(mock_check_output):
    mock_check_output.return_val = 'Link Quality=60/70  Signal level=-55 dBm'
    monitor = WifiMonitor()
    assert monitor.get_Signal_dbm() == -55
 def test_signal_missing(mock_check_output):
     mock_check_output.return_val = 'no signal here'
     monitor = WifiMonitor()
     with pytest.raises(ValueError):
         monitor.get_Signal_dbm()
         