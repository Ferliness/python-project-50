install:
	poetry install

gendiff_run:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall dist/*.whl

lint:
	poetry run flake8 gendiff