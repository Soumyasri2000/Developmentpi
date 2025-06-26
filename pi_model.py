def get_pi_model() -> str:
    try:
        with open('/proc/device-tree/model','rb') as f:
            return f.read().decode('utf-8', errors='ignore').strip()
    except Exception:
        return "Unknown"
        
def is_zero2w() -> bool:
    model = get_pi_model()
    return "Zero 2 W" in model or "Zero2W" in model