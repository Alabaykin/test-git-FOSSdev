VENV = .venv
PYTHON_BIN = $(if $(wildcard $(VENV)/Scripts/python.exe),$(VENV)/Scripts,$(VENV)/bin)
PYTHON = $(PYTHON_BIN)/python
PIP = $(PYTHON_BIN)/pip

$(VENV):
	python3 -m venv $(VENV) || python -m venv $(VENV)

install: $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e .[dev]

test: install
	$(PYTHON) -m pytest tests/

check-requirements: install
	$(PYTHON_BIN)/deptry src/

typecheck: install
	$(PYTHON_BIN)/mypy src/

lint: install
	$(PYTHON_BIN)/flake8 src/

check: lint typecheck check-requirements test

build: install
	$(PYTHON) -m build

docs:
	@echo "Documentation is provided in README.md"

publish: build
	$(PYTHON_BIN)/twine check dist/*
	$(PYTHON_BIN)/twine upload --repository testpypi dist/*