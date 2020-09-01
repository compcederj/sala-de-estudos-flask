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
	pip install -e .[dev] --upgrade --no-cache

format:
	isort **/*.py
	black -l 79 **/*.py

install:
	pip install -e .

install-dev:
	poetry install

run-dev:
	FLASK_APP=sala_de_estudos_flask/app.py FLASK_ENV=development flask run

run:
	gunicorn 'holiday_api.app:create_app()'

test:
	FLASK_APP=sala_de_estudos_flask/app.py FLASK_ENV=test flask create-database
	FLASK_APP=sala_de_estudos_flask/app.py FLASK_ENV=test pytest tests/ -v --cov=holiday_api
	FLASK_APP=sala_de_estudos_flask/app.py FLASK_ENV=test flask drop-database
