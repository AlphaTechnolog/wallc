import json
from util.consts import Consts

class ConfigChecker:
    _config_path = Consts().get('config_path')

    def __init__(self):
        self._load__config()

    def _load__config(self):
        with open(self._config_path, 'r') as raw_config:
            self._config = json.load(raw_config)

    def check(self, *args):
        for key in args:
            try:
                self._config[key]
            except (KeyError):
                return False

        return True
