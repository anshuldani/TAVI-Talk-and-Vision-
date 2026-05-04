.PHONY: setup setup-backend setup-frontend run-backend run-frontend test lint clean

PYTHON ?= python3
PIP    ?= $(PYTHON) -m pip

setup: setup-backend setup-frontend

setup-backend:
	$(PIP) install -r backend/requirements.txt

setup-frontend:
	$(PIP) install -r frontend/requirements.txt

run-backend:
	cd backend && uvicorn app:app --reload --port 8000

run-frontend:
	cd frontend && $(PYTHON) main.py

test:
	$(PYTHON) -m pytest tests/ -v

lint:
	$(PYTHON) -m pyflakes backend/ frontend/ tests/ || true

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	rm -rf backend/temp_uploads frontend/temp_uploads
