from os import remove
from os.path import isfile
from cli_app import Command
from util.consts import Consts
from util.config import ConfigChecker, ConfigGetter
from util.messages import error, success

class Rm(Command):
    """Remove a wallpaper by name and extension."""

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('name', help='The wallpaper name.')
        parser.add_argument(
            '-e', '--extension', required=False,
            default='jpg', help='The wallpaper extension.'
        )

    def _create__config_consts(self):
        self.config_path = Consts().get('config_path')
        self.config_checker = ConfigChecker()
        self.config = ConfigGetter(self.config_path)
        self.config = self.config.prconfig()

    def _check__config_rules(self):
        if not self.config_checker.check('wallpaper_path'): 
            error(
                'Invalid config rules',
                'Please before delete an image',
                'set the wallpapers path, exec:',
                '$ wallc config -wp <WALLPAPERS_PATH>'
            )

    def _get__complete_wallpaper_path(self):
        wallpapers_path = self.config['wallpaper_path']
        full_wall_path = wallpapers_path + self.app.args.name
        full_wall_path = full_wall_path + '.' + self.app.args.extension
        return full_wall_path

    def _remove_wallpaper(self):
        if not isfile(self.complete_wall_path):
            error(
                'Invalid wallpaper path',
                self.complete_wall_path,
                'Please pass a valid file name or extension'
            )

        remove(self.complete_wall_path)

        success(
            'Deleted the wallpaper',
            self.complete_wall_path,
            'successfully!'
        )

    def run(self):
        self._create__config_consts()
        self._check__config_rules()
        self.complete_wall_path = self._get__complete_wallpaper_path()
        self._remove_wallpaper()
