from cli_app import App
from commands.manage import Manage
from commands.config import Config
from commands.set import Set

class Pytrogen(App):
    """Nitrogen writed in python"""

    def register_commands(self):
        self.add_command('manage', Manage)
        self.add_command('config', Config)
        self.add_command('set', Set)

if __name__ == '__main__':
    app = Pytrogen()
    app.run()
