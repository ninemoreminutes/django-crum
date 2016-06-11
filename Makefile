.PHONY: core-requirements update-pip-requirements requirements \
	clean-pyc develop check migrate runserver reports pep8 flake8 check8 \
	test ship-it

core-requirements:
	pip install "pip>=8,<8.1.2" "setuptools>=20" "pip-tools>=1.6,<1.7"

update-pip-requirements: core-requirements
	pip-compile --upgrade requirements.in

requirements: core-requirements
	pip-sync requirements.txt

clean-pyc: requirements
	find . -iname "*.pyc" -delete

develop: clean-pyc
	python setup.py develop

check: develop
	python manage.py check

migrate: check
	python manage.py migrate --noinput --fake-initial

runserver: migrate
	python manage.py runserver

test: clean-pyc
	python setup.py test

tox: clean-pyc
	tox

ship-it: clean-pyc
	python setup.py release_build register upload upload_docs
