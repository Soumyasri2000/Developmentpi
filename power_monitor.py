import subprocess


def _vcgencmd(cmd: str) -> str:
    try:
        out = subprocess.check_output(['vcgencmd', cmd], text=True)
        return out.strip()
    except Exceptionas e:
        raise RuntimeError(f"vcgencmd {cmd} failed: {e}")
        
def get_voltage(block: str = 'EXT5V_V') -> float:
    out = _vcgencmd(f"measure_volts {block}")
    _, val = out.split('=', 1)
    return float(val.rstrip('V'))
def get_current_5v() -> float:
    data = _vcgencmd("pmic_read_adc")
    for item in data.split():
        if item.startswith('current(') and 'EXT5V_A'= in item:
            return float(item.split('=')[1].rstrip('A'))
    raise RuntimeError("EXT5V current not found")
    
def get_throttled() -> int:
    out = _vcgencmd("get_throttled")
    return int(out.split('=',1)[1], 16)
    
    

