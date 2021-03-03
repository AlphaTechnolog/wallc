from cli_app import Command
from util.consts import Consts

class Set(Command):
    """Set config."""

    config_path = Consts().get('config_path')

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('-w', '--wallpaper', required=True, help='Wallpaper name.')

    def run(self):
        print(self.config_path)
