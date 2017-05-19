.PHONY: core-requirements update-pip-requirements requirements \
	clean-pyc develop check migrate runserver reports pep8 flake8 check8 \
	test clean-tox tox clean-all ship-it

core-requirements:
	pip install "pip>=9,<10" "setuptools>=20" "pip-tools>=1.9,<2"

update-pip-requirements: core-requirements
	pip-compile --upgrade requirements.in

requirements: core-requirements
	pip-sync requirements.txt

clean-pyc: requirements
	find . -iname "*.pyc" -delete
	find . -iname __pycache__ | xargs rm -rf

develop: clean-pyc
	python setup.py develop

check: develop
	python manage.py check

migrate: check
	python manage.py migrate --noinput --fake-initial

runserver: migrate
	python manage.py runserver

reports:
	mkdir -p $@

pep8: reports requirements
	set -o pipefail && $@ | tee reports/$@.report

flake8: reports requirements
	set -o pipefail && $@ | tee reports/$@.report

check8: pep8 flake8

test: clean-pyc
	python setup.py test

clean-tox:
	rm -rf .tox

tox: clean-pyc
	tox

clean-all: clean-pyc clean-tox
	rm -rf *.egg-info .eggs .cache .coverage build reports

ship-it: clean-pyc
	python setup.py release_build register upload upload_docs
