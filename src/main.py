#!/usr/bin/env python3

from cli_app import App
from commands.manage import Manage
from commands.config import Config
from commands.show import Show
from commands.rm import Rm
from commands.set import Set
from commands.download import Download

class Wallc(App):
    """Manage your wallpapers, with a wallpapers server"""

    def register_commands(self):
        self.add_command('manage', Manage)
        self.add_command('config', Config)
        self.add_command('set', Set)
        self.add_command('show', Show)
        self.add_command('rm', Rm)
        self.add_command('download', Download)

if __name__ == '__main__':
    app = Wallc()
    app.run()
