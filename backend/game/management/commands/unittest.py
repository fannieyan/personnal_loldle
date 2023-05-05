from django.core.management.commands.test import Command as TCommand


class Command(TCommand):

    def execute(self, *args, **options):
        test_class = 'game.runner.unittest.UnitTestRunner'
        options['testrunner'] = test_class
        super().execute(*args, **options)
