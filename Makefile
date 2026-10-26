.PHONY: install run test lint clean

install:
	pip install -e ".[dev]"

run:
	uvicorn backend.main:app --reload --port 8000

test:
	pytest -v

lint:
	ruff check backend tests

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -f uploads/*.pdf uploads/*.docx uploads/*.pptx
