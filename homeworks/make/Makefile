VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install -r requirements.txt

run: install
	$(PYTHON) src/app.py

check-requirements: install
	$(VENV)/bin/pip-missing-reqs --ignore-module=app src/