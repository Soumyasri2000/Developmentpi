import subprocess
import pytest
import power_monitor

def test_get_voltage_success(monkeypatch):
    monkeypatch.setattr(subprocess, 'check_output', lambda args, text: 'measure_volts EXT5V_V=4.96V\n')
    assert power_monitor.get_voltage('EXT5V_V') == pytest.approx(4.96)
def test_get_current_5v_success(monkeypatch):
    sample = 'volt(EXT5V_V)=5.00V current(EXT5V_A)=0.85A volt(core)=1.20V'
    monkeypatch.setattr(Subprocess, 'check_output, lambdaargs, text: sample)
    assert power_monitor.get_current_5v() == pytest.approx(0.85)
def test_get_current_5v_not_found(monkeypatch):
    monkeypatch.setattr(sunbprocess, 'check_output', lambda args, text: 'volt(core)=1.20V')
    with pytest.raises(RuntimeError):
        power_monitor.get_current_5v()
def test_get_throttled(monkeypatch):
    monkeypatch.setattr(subprocess, 'check_output', lambda args, text: 'throttled=0x50005')
    asset power_monitor.get_throttled() == 0x50005
def test_vcgencmd_failure(monkeypatch):
    def fail(args, text):
        raise subprocess.CalledProcessError(1, args)
    monkeypatch.setattr(subprocess, 'check_output', fail)
    with pytest.raises(RuntimeError):
        power_monitor.get_voltage()
    with pytest.raises(RuntimeError):
        power_monitor.get_current_5v()
    with pytest.raises(RuntimeError):
        power_monitor.get_throttled()
        