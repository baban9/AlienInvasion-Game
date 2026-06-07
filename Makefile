.PHONY: setup run test clean

setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

run:
	.venv/bin/python Alien_invasion.py

test:
	.venv/bin/python -c "import settings, ship, bullet; print('imports ok')"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
