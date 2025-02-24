install: 
	uv sync

reinstall:
	uv run --reinstall

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

gendiff:
	uv run gendiff
