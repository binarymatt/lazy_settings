import os
from ConfigParser import ConfigParser
def guess_bool(value):
    if isinstance(value, str):
        if value.lower() is 'true':
            return True
        elif value.lower() is 'false':
            return False
    raise Exception('Bad boolean')

class LazySettings(object):
    def __init__(self, settings_path=None):
        self.settings_path = settings_path or os.path.join(os.path.dirname(os.path.abspath(__file__)),'settings.ini')
        self._setup()
    
    def _setup(self):
        conf_path = os.environ.get('LAZY_CONF', self.settings_path)
        config = ConfigParser()
        config.read(conf_path)
        for key,value in config.items('Main'):
            setattr(self,key.upper(), self._guess_type(value))
    
    def _guess_type(self, value):
        object_types = [int, float, guess_bool]
        val = None
        for func in object_types:
            try:
                val = func(value)
            except:
                pass
        return val