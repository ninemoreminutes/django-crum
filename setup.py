#!/usr/bin/env python

# Python
import os
import sys

# Setuptools
from setuptools import setup, find_packages

# Django-CRUM
from crum import __version__

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
    # extra['convert_2to3_doctests'] = ['src/your/module/README.txt']
    # extra['use_2to3_fixers'] = ['your.fixers']

setup(
    name='django-crum',
    version=__version__,
    author='Nine More Minutes, Inc.',
    author_email='support@ninemoreminutes.com',
    description='Django middleware to capture current request and user.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst'),
                          'rb').read().decode('utf-8'),
    license='BSD',
    keywords='django request user middleware thread local',
    url='https://github.com/ninemoreminutes/django-crum/',
    packages=find_packages(exclude=['test_project']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'django',
        'djangorestframework',
        'pytest',
        'pytest-cov',
        'pytest-django',
        'pytest-flake8',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    options={
        'egg_info': {
            'tag_svn_revision': 0,
            'tag_build': '.dev',
        },
        'build_sphinx': {
            'source_dir': 'docs',
            'build_dir': 'docs/_build',
            'all_files': True,
            'version': __version__,
            'release': __version__,
        },
        'upload_sphinx': {
            'upload_dir': 'docs/_build/html',
        },
        'upload_docs': {
            'upload_dir': 'docs/_build/html',
        },
        'aliases': {
            'dev_build': 'egg_info sdist build_sphinx',
            'release_build': 'egg_info -b "" -R sdist build_sphinx',
            'test': 'pytest',
        },
    },
    **extra
)
