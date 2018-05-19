.PHONY: core-requirements
core-requirements:
	pip install "pip>=9" "setuptools>=20" "pip-tools>=1.9"

.PHONY: update-pip-requirements
update-pip-requirements: core-requirements
	pip install -U "pip>=9" "setuptools>=20" "pip-tools>=1.9"
	pip-compile --upgrade requirements.in

.PHONY: requirements
requirements: core-requirements
	pip-sync requirements.txt

.PHONY: clean-pyc
clean-pyc: requirements
	find . -iname "*.pyc" -delete
	find . -iname __pycache__ | xargs rm -rf

.PHONY: develop
develop: clean-pyc
	python setup.py develop

.PHONY: check
check: develop
	python manage.py check

.PHONY: migrate
migrate: check
	python manage.py migrate --noinput

.PHONY: runserver
runserver: migrate
	python manage.py runserver

reports:
	mkdir -p $@

.PHONY: pycodestyle
pycodestyle: reports requirements
	set -o pipefail && $@ | tee reports/$@.report

.PHONY: flake8
flake8: reports requirements
	set -o pipefail && $@ | tee reports/$@.report

.PHONY: check8
check8: pycodestyle flake8

.PHONY: test
test: clean-pyc
	python setup.py test

.PHONY: clean-tox
clean-tox:
	rm -rf .tox

.PHONY: tox
tox: clean-pyc
	tox

.PHONY: clean-all
clean-all: clean-pyc clean-tox
	rm -rf *.egg-info .eggs .cache .coverage build reports

.PHONY: bump-major
bump-major: requirements
	bumpversion major

.PHONY: bump-minor
bump-minor: requirements
	bumpversion minor

.PHONY: bump-patch
bump-patch: requirements
	bumpversion patch

.PHONY: docs
docs: requirements
	python setup.py build_sphinx

.PHONY: ship-it
ship-it: clean-pyc
	python setup.py release_build register upload upload_docs
