import json
import subprocess
from os.path import isfile
from cli_app import Command
from util.consts import Consts
from util.messages import success, error
from util.config import ConfigChecker

class Set(Command):
    """Set config."""

    config_path = Consts().get('config_path')

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('-w', '--wallpaper', required=True, help='Wallpaper name.')
        parser.add_argument('-e', '--extension', required=False, help='Wallpaper extension.',
                            default='jpg')

    def _check__config_keys(self):
        config_checker = ConfigChecker()

        if not config_checker.check('wallpaper_path'):
            error(
                'Invalid config rules!',
                'Please before config the wallpaper_path!, use:',
                '$ wallc config -wp <WALLPAPER_PATH>'
            )

    def _set__wallpaper__in_config(self):
        with open(self.config_path, 'r') as raw_config:
            existent_config = json.load(raw_config)

        wall_path = existent_config['wallpaper_path']
        args = self.app.args
        wall_name = args.wallpaper + '.' + args.extension
        wallpaper = wall_path + wall_name

        existent_config['wallpaper'] = wallpaper
        self.existent_config = existent_config

        with open(self.config_path, 'w') as raw_config:
            json.dump(existent_config, raw_config)

    def _set__wallpaper(self):
        wall_path = self.existent_config['wallpaper_path']
        args = self.app.args
        wall_name = args.wallpaper + '.' + args.extension
        wall_url = wall_path + wall_name

        if isfile(wall_url):
            subprocess.run(
                [f'feh --bg-scale {wall_url}'],
                shell=True,
                stdout=subprocess.PIPE
            )
        else:
            error(
                'Invalid wallpaper url:',
                wall_url
            )

        success(
            'Updated background to',
            wall_url
        )

    def run(self):
        self._check__config_keys()
        self._set__wallpaper__in_config()
        self._set__wallpaper()
