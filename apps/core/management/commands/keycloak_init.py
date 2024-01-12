from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'KeyCloak Realm 数据初始化'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('初始化KeyCloak Realm......')
        pass
