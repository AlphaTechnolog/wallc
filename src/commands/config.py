import json
from cli_app import Command
from util.consts import Consts
from util.messages import success


class Greeter:
    def __init__(self: Callable, name: str) -> Callable:
        self.name = name

    def greet(self: Callable):
        print(f'Hello {name}')


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

        parser.add_argument(
            '-dp',
            '--download-path',
            required=False,
            type=str,
            help='The download wallpapers path'
        )

    def _process__path(self, path):
        if not path.endswith('/'):
            return path + '/'
        else:
            return path

    def config__wallpaper_path(self):
        with open(self.config_path) as raw_config:
            existent_config = json.load(raw_config)

        self.app.args.wallpaper_path = self._process__path(
            self.app.args.wallpaper_path
        )
        
        existent_config['wallpaper_path'] = (
            self.app.args.wallpaper_path
        )

        with open(self.config_path, 'w') as raw_config:
            json.dump(existent_config, raw_config)

        success(
            'Configuration reloaded!',
            'The wallpaper path was uploaded to',
            self.app.args.wallpaper_path
        )

    def config__download_path(self):
        with open(self.config_path) as raw_config:
            existent_config = json.load(raw_config)

        self.app.args.download_path = self._process__path(
            self.app.args.download_path
        )

        existent_config['download_path'] = (
            self.app.args.download_path
        )

        with open(self.config_path, 'w') as raw_config:
            json.dump(existent_config, raw_config)

        success(
            'Configuration reloaded!',
            'The download path was updated to',
            self.app.args.download_path
        )

    def run(self):
        if self.app.args.wallpaper_path:
            self.config__wallpaper_path()

        if self.app.args.download_path:
            self.config__download_path()
