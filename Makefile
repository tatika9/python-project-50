lint:
	poetry run flake8 gendiff
test:
	poetry run pytest -vv
install:
	poetry install
	poetry build
	python3 -m pip install --user dist/*.whl
check: lint test
test-coverage:
	poetry run pytest --cov=gendiff  --cov-report xml
