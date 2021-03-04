import json
import subprocess
from os.path import isfile
from cli_app import Command
from util.consts import Consts
from util.messages import error, success
from util.config import ConfigChecker

class Manage(Command):
    """General Commands."""

    config_path = Consts().get('config_path')
    config_checker = ConfigChecker()

    @staticmethod
    def register_arguments(parser):
        parser.add_argument(
            '--restore',
            action='store_true'
        )

    def _register__config(self):
        with open(self.config_path, 'r') as raw_config:
            self.config = json.load(raw_config)

    def _manage__restore__check__config_rules(self):
        if not self.config_checker.check('wallpaper_path', 'wallpaper'):
            error(
                'Invalid config rules!',
                'Please before set a wallpaper with order:',
                '$ pytrogen set -w <WALLPAPER_NAME> -e <WALLPAPER_EXTENSION>'
            )

    def _manage__restore__load__wallpaper(self):
        wallpaper = self.config['wallpaper']

        if isfile(wallpaper):
            subprocess.run(
                [f'feh --bg-scale {wallpaper}'],
                shell=True,
                stdout=subprocess.PIPE
            )
        else:
            error(
                'Invalid wallpaper url!',
                f'The wallpaper url: {wallpaper}',
                'is invalid, please update it manually',
                'editing the file ~/.pytrogen.conf.json',
                'or use instead:',
                '$ pytrogen config -wp <WALLPAPER_PATH>',
                '$ pytrogen set -w <WALLPAPER_NAME> -e <WALLPAPER_EXTENSION>'
            )

        success(
            'Restored the wallpaper',
            wallpaper,
            'successfully!'
        )

    def _manage__restore(self):
        self._manage__restore__check__config_rules()
        self._manage__restore__load__wallpaper()

    def run(self):
        self._register__config()

        if self.app.args.restore:
            self._manage__restore()
