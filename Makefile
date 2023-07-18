lint:
	poetry run flake8 gendiff
test:
	poetry run pytest -vv
install:
	poetry install
check: lint test
test-coverage:
	poetry run pytest --cov=gendiff  --cov-report xml
.PHONY: lint test install check