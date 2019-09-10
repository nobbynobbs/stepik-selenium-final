review-tests:
	python -m pytest -v --tb=line --language=en -m need_review --headless

all-tests:
	python -m pytest -v --tb=line --language=en

all-tests-headless:
	python -m pytest -v --tb=line --language=en --headless
