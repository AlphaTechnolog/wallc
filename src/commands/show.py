import json
import re
from cli_app import Command
from os import scandir
from util.consts import Consts
from util.messages import error, info
from util.config import ConfigChecker
from colorama import init, Fore

init(autoreset=True)

class Show(Command):
    """Show the available wallpapers"""

    config_path = Consts().get('config_path')
    config_checker = ConfigChecker()

    @staticmethod
    def register_arguments(parser):
        parser.add_argument(
            '--filter', required=False,
            choices=('name', 'extension',), help='Filter by.'
        )

        parser.add_argument(
            '--filter-value',
            required=False,
            help='Value of filter.'
        )

    def _check__config_rules(self):
        if not self.config_checker.check('wallpaper_path'):
            error(
                'Invalid config rules!',
                'Please before set the wallpapers path!, use this command',
                '$ wallc config -wp <WALLPAPER_PATH>'
            )

    def _check__filters(self):
        if self.app.args.filter is not None:
            if self.app.args.filter_value is None:
                error(
                    'Invalid filter value',
                    'Please pass the --filter-value flag',
                    'to indicate the value of filter: "{}"'.format(
                        self.app.args.filter
                    )
                )

    def _get__wallpapers_list(self):
        with open(self.config_path, 'r') as raw_config:
            config = json.load(raw_config)

        wallpapers_path = config['wallpaper_path']
        self.wallpaper = config['wallpaper']
        self.wallpapers_path = wallpapers_path
        wallpapers_list = dict()

        for archive in scandir(wallpapers_path):
            if archive.is_file():
                arname = archive.name.split('.')[0]
                arext = archive.name.split('.')[1]
                if (arext == 'png' or
                        arext == 'jpg'):
                    wallpapers_list[arname] = arext

        return wallpapers_list

    def _get__wallpapers_list__by_filter(self):
        wallpapers_base = self._get__wallpapers_list()
        wallpapers_base = list(wallpapers_base.items())
        wallpapers_base.sort()

        filter_result = dict()

        for wallpaper, extension in wallpapers_base:
            validation_value = wallpaper if self.app.args.filter == 'name' else extension
            if validation_value == self.app.args.filter_value:
                filter_result[wallpaper] = extension

        return filter_result
    
    def _show__wallpapers(self, wallpapers):
        info('Showing wallpapers available in {}'.format(
            self.wallpapers_path
        ))

        wallpapers = list(wallpapers.items())
        wallpapers.sort()

        for wallpaper, extension in wallpapers:
            wallpapers_path = self.wallpapers_path
            full_wallpaper_path = wallpapers_path + wallpaper
            full_wallpaper_path = full_wallpaper_path + '.' + extension
            active_wallpaper = self.wallpaper

            if active_wallpaper == full_wallpaper_path:
                wall_string = f'{Fore.GREEN}*{wallpaper}*{Fore.YELLOW}'
            else:
                wall_string = f' {wallpaper} '

            print(
                f"{Fore.YELLOW}  -> {wall_string} {f'= {extension}' if extension != 'jpg' else ''}"
            )

    def run(self):
        self._check__config_rules()
        self._check__filters()

        if self.app.args.filter is None:
            wallpapers = self._get__wallpapers_list()
        else:
            wallpapers = self._get__wallpapers_list__by_filter()

        self._show__wallpapers(wallpapers)
