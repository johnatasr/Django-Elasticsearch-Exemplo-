from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from django_elasticsearch_example.utils import wait_elasticsearch_availability

class Command(BaseCommand):
    help = '''
    Setup project.
     - apply migrations
     - loaddata
     - create and populate index and mapping
    '''

    def handle(self, *args, **options):
        print('Verifi viabilidade')
        wait_elasticsearch_availability()
        try:
            call_command('migrate', '--noinput')
            print('Migrando ..')
            call_command('loaddata', 'manufacturers.json')
            print('Carregando manufacturers.json')
            call_command('loaddata', 'cars.json')
            print('Carregando cars.json')
            call_command('search_index', '--rebuild', '-f')
            print('Carregando Index')
        except Exception as exception:
            raise CommandError(
                'Something went wrong during executing commands: {}'.format(
                    exception
                )
            )
        self.stdout.write(self.style.SUCCESS('Successfully ended commands'))
