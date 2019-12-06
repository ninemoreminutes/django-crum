#!/usr/bin/env python

# Setuptools
from setuptools import Command, setup


class BaseTwineCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.run_command('sdist')
        self.get_finalized_command('sdist')
        self.run_command('bdist_wheel')
        self.get_finalized_command('bdist_wheel')
        dist_files = [df[2] for df in self.distribution.dist_files]
        self.spawn(['twine', self.twine_subcommand] + dist_files)

    sub_commands = [
        ('sdist', lambda self: True),
        ('bdist_wheel', lambda self: True),
    ]


class TwineCheckCommand(BaseTwineCommand):

    description = 'Check distribution files with twine'
    twine_subcommand = 'check'


class TwineUploadCommand(BaseTwineCommand):

    description = 'Upload distribution files with twine'
    twine_subcommand = 'upload'


setup(
    cmdclass={
        'twine_check': TwineCheckCommand,
        'twine_upload': TwineUploadCommand,
    },
)
