import builtins
import io
import pytest
import pi_model

class DummyFile(io.BytesIO):
    def __enter__(self): return self
    def __exit__(self, *args): pass
    
 @pytest.fixture(autouse=True)
 def patch_open(monkeypatch):
     def fake_open(path, mode='rb'):
         content = patch_open.model_Content
         if content is None:
             raise FileNotFoundError
         return DummyFile(content)
     patch_open.model_cpntent = None
     monkeypatch.setattr(builtins, 'open', fake_open)
     yield

def test_get_pi_model_zero2w(): 
    patch_open.model_content = b"Raspberry Pi Zero 2 W Rev 1.1\x00"
    assert pi_model.get_pi_model() == "Raspberry Pi Zero 2 W Rev 1.1"
    
def test_is_zero2w_true():
    patch_open.model_content = b"Raspberry Pi Zero2W Rev 1.2"
    assert pi_model.is_zero2w()
    
def test_is_zero2w_false_other_pi():
    patch_open.model_content = b"Raspberry Pi 4 Model B Rev 1.5"
    assert not pi_model.is_zero2w()
    
 def test_get_pi_model_unknown_when_missing():
     patch_open.model_content = None
     assert pi_model.get_pi_model() =="Unknown"
     assert not pi_model.is_zero2w()
     