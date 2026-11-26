.PHONY = install run clean lint lint-strict
.DEFAULT_GOAL = run

src_dir = src
mypy_flags = --warn-return-any \
			 --warn-unused-ignores \
			 --ignore-missing-imports \
			 --disallow-untyped-defs \
			 --check-untyped-defs

install:
	uv sync

run: install
	uv run python3 -m $(src_dir) 

debug:
	uv run python3 -m pdb -m $(src_dir)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {}
	rm -rf .mypy_cache

lint:
	uv run flake8 . --exclude=.venv/
	uv run mypy . $(mypy_flags)

lint-strict:
	uv run flake8 . --exclude=.venv/
	uv run mypy . --strict
