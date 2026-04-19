VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install -r requirements.txt
	$(PIP) install deptry mypy flake8

run: install
	$(PYTHON) src/app.py

check-requirements: install
	$(VENV)/bin/deptry src/

typecheck: install
	$(VENV)/bin/mypy src/

lint: install
	$(VENV)/bin/flake8 src/

check: lint typecheck check-requirements