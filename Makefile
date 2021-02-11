clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	python -m pip install -e .[dev] --upgrade --no-cache

format:
	dephell deps convert
	python -m isort -l 119 **/*.py
	python -m black -l 119 **/*.py

install:
	python -m pip install -e .

install-dev:
	poetry install

run-dev:
	FLASK_APP=sala_de_estudos_flask/app.py FLASK_ENV=development flask run

run:
	gunicorn 'sala_de_estudos_flask.app:create_app()'

test:
	FLASK_APP=sala_de_estudos_flask/app.py FLASK_ENV=test flask create-database
	FLASK_APP=sala_de_estudos_flask/app.py FLASK_ENV=test pytest tests/ -v --cov=sala_de_estudos_flask
	FLASK_APP=sala_de_estudos_flask/app.py FLASK_ENV=test flask drop-database
