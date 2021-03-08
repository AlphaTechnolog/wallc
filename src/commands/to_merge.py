from cli_app import Command
from util.config import ConfigGetter
from util.consts import consts
from util.messages import error, info
from colorama import init, Fore

init(autoreset=True)

class ToMerge(Command):
    """Show the wallpapers to merge."""

    config = ConfigGetter(
        consts.get('config_path')
    ).prconfig()

    @staticmethod
    def register_arguments(parser):
        parser.add_argument('--show-help', '-sh', action='store_true')

    def _check__meta(self):
        if not 'meta' in self.config:
            error(
                'Invalid order',
                'no to merge operations'
            )

    def _show__help(self):
        info(
            'To apply the merge use',
            'the next command',
            '$ wallc download --merge MERGE_ID'
        )

        print()

    def _show(self, merge_list):
        info('To merge list:')

        for merge_id, merge_name in list(merge_list.items()):
            print("{}  -> {} = {}".format(
                Fore.YELLOW,
                merge_name,
                merge_id
            ))

    def run(self):
        self._check__meta()

        if self.app.args.show_help:
            self._show__help()

        self._show(self.config['meta'])
