import json
import requests
from cli_app import Command
from util.config import ConfigChecker, ConfigGetter
from util.messages import error, success, info
from util.consts import consts
from shutil import move as mv

class Download(Command):
    """Use the wallc marketplace to download the wallpapers."""

    config_checker = ConfigChecker()
    marketplace = consts.get('marketplace')
    config_path = consts.get('config_path')

    config = ConfigGetter(
        consts.get('config_path')
    ).prconfig()

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('id', help='The wallpaper id')
        parser.add_argument('--merge', action='store_true')

    def _checks(self):
        if (not self.config_checker.check(
            'wallpaper_path',
            'download_path'
        )):
            error(
                'This action is unavailable',
                'to unlock it, config the',
                'download_path && wallpaper_path rules',
                'use:',
                '$ wallc config -wp WALL_PATH -dp DOWNLOAD_PATH'
            )

    def merge_wallpapers(self):
        with open(self.config_path, 'r') as raw_config:
            config = json.load(raw_config)

        if not 'meta' in config:
            error(
                'Nothing to merge'
            )

        if not self.app.args.id in config['meta']:
            error(
                'Invalid id to merge'
            )

        wall_ext = config['meta'][self.app.args.id]
        wall_ext = wall_ext.split('.')[-1]
        wall_name = self.app.args.id + '.' + wall_ext

        wall_uri = (
            config['download_path'] +
            wall_name
        )

        new_wall_uri = (
            config['wallpaper_path'] +
            config['meta'][self.app.args.id]
        )

        info(
            'Moving the wallpaper ' + config['meta'][self.app.args.id],
            'from ' + wall_uri,
            'to ' + new_wall_uri
        )

        mv(
            wall_uri,
            new_wall_uri
        )

        success(
            'Moved the wallpaper',
            config['meta'][self.app.args.id]
        )

        info(
            'Refreshing merge meta information',
            'into your config file:',
            self.config_path
        )

        del config['meta'][self.app.args.id]

        if len(config['meta']) == 0:
            del config['meta']

        with open(self.config_path, 'w') as raw_config:
            json.dump(config, raw_config)

        success(
            'Refreshed your merge config',
            'Merged the wallpaper with id',
            self.app.args.id
        )

    def download_wallpaper(self):
        info(
            'Please wait, downloading wallpaper',
            self.app.args.id
        )

        uri = self.marketplace + '/images/' + (
            self.app.args.id
        )

        meta_request = requests.get(uri)
        meta_request = meta_request.json()

        image_blob = requests.get(
            meta_request['src'],
            stream=True
        )

        ext = meta_request['name'].split('.')[-1]

        image_uri = self.config['download_path'] + (
            meta_request['_id'] + '.' + ext
        )

        image = open(image_uri, 'wb')

        for chunk in image_blob.iter_content(chunk_size=256):
            if chunk:
                image.write(chunk)

        success(
            'Downloaded the wallpaper in',
            image_uri
        )

        info(
            'Updating meta data in the config',
            'this process take your config and add',
            'rules of wallpaper merge name process',
            'please wait a few moments.'
        )

        with open(self.config_path, 'r') as raw_config:
            config = json.load(raw_config)

        if not 'meta' in config:
            config['meta'] = dict()

        config['meta'][meta_request['_id']] = meta_request['name']

        with open(self.config_path, 'w') as raw_config:
            json.dump(config, raw_config)

        success(
            'Updated meta information in your',
            'config file, to merge the files use:',
            '$ wallc download --merge {}'.format(
                self.app.args.id
            )
        )

    def run(self):
        self._checks()

        if self.app.args.merge:
            self.merge_wallpapers()
        else:
            self.download_wallpaper()
