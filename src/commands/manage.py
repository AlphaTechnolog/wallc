from cli_app import Command

class Manage(Command):
    """General Commands."""

    @staticmethod
    def register_arguments(parser):
        parser.add_argument(
            '--restore',
            action='store_true'
        )

    def run(self):
        print(self.app.args)
