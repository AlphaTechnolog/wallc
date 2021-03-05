import json
from cli_app import Command
from util.consts import Consts
from util.messages import success

class Config(Command):
    """Manage the wallc config."""

    config_path = Consts().get('config_path')

    @staticmethod
    def register_arguments(parser):
        parser.add_argument(
            '-wp',
            '--wallpaper-path',
            required=False,
            type=str,
            help='The wallpapers path'
        )

    def _process__wallpaper_path(self):
        if not self.app.args.wallpaper_path.endswith('/'):
            return self.app.args.wallpaper_path + '/'
        else:
            return self.app.args.wallpaper_path

    def config__wallpaper_path(self):
        with open(self.config_path) as raw_config:
            existent_config = json.load(raw_config)

        self.app.args.wallpaper_path = self._process__wallpaper_path()
        existent_config['wallpaper_path'] = self.app.args.wallpaper_path

        with open(self.config_path, 'w') as raw_config:
            json.dump(existent_config, raw_config)

        success(
            'Configuration reloaded!',
            'The wallpaper path was uploaded to',
            self.app.args.wallpaper_path
        )

    def run(self):
        if self.app.args.wallpaper_path:
            self.config__wallpaper_path()
