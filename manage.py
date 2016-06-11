#!/usr/bin/env python

# Python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')
    import django
    django.setup()

    # Use the runserver addr/port defined in settings.
    from django.conf import settings
    default_addr = getattr(settings, 'RUNSERVER_DEFAULT_ADDR', '127.0.0.1')
    default_port = getattr(settings, 'RUNSERVER_DEFAULT_PORT', 8000)
    from django.core.management.commands import runserver as core_runserver
    original_handle = core_runserver.Command.handle

    def handle(self, *args, **options):
        if not options.get('addrport'):
            options['addrport'] = '%s:%d' % (default_addr, int(default_port))
        elif options.get('addrport').isdigit():
            options['addrport'] = '%s:%d' % (default_addr, int(options['addrport']))
        return original_handle(self, *args, **options)

    core_runserver.Command.handle = handle

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
