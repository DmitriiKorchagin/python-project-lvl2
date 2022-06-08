install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run pytest -vv

test-cov:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

lint:
	poetry run flake8 gendiff
