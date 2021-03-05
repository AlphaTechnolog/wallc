from colorama import init, Fore

init(autoreset=True)

class BaseLog:
    _options = {}
    _args = []

    def __init__(self, *args):
        self._args = args

    def update(self, key, val):
        self._options[key] = val

    def log(self):
        if len(self._args) == 1:
            print(f'{self._options["color"]}{self._options["prefix"]}: {self._args[0]}')
        else:
            print(f'{self._options["color"]}{self._options["prefix"]}:')

        if len(self._args) != 1:
            for msg in self._args:
                print(f'{self._options["secondary_color"]}  > {msg}')

        if self._options['exit']:
            exit(1)

def success(*args):
    base_log = BaseLog(*args)
    base_log.update('prefix', '[SUCCESS]')
    base_log.update('exit', False)
    base_log.update('color', Fore.GREEN)
    base_log.update('secondary_color', Fore.YELLOW)
    base_log.log()

def error(*args):
    base_log = BaseLog(*args)
    base_log.update('prefix', '[ERROR]')
    base_log.update('exit', True)
    base_log.update('color', Fore.RED)
    base_log.update('secondary_color', Fore.MAGENTA)
    base_log.log()

def info(*args):
    base_log = BaseLog(*args)
    base_log.update('prefix', '[INFO]')
    base_log.update('exit', False)
    base_log.update('color', Fore.BLUE)
    base_log.update('secondary_color', Fore.RESET)
    base_log.log()
