run:
	uv run fastapi dev src/{{cookiecutter.project_slug}}/server/main.py

test:
	uv run pytest

check:
	uvx ruff format
	uvx ruff check --fix
	uv run mypy src tests

