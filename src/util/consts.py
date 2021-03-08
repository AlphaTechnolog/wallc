import json
from util.files import path
from os.path import isfile

class Consts:
    consts = {}

    def __init__(self):
        self.new_const(
            'config_path',
            path('~/.wallc.conf.json'),
            self._cb__conf_path_cb
        )

        self.new_const('marketplace', 'http://localhost:8080/api', self._pass_func)

    def _pass_func(self, varname, config_path):
        pass

    def _cb__conf_path_cb(self, varname, config_path):
        if not isfile(config_path):
            open(config_path, 'x')
            with open(config_path, 'w') as raw_config:
                json.dump({}, raw_config)

    def new_const(self, name, value, cb):
        if cb:
            cb(name, value)

        self.consts[name] = value

    def get(self, name):
        return self.consts[name]

consts = Consts()
