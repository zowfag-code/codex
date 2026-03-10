.PHONY: test check run

test:
	python -m unittest discover -s tests -p 'test_*.py' -v

check:
	python -m compileall src tests
	python -m unittest discover -s tests -p 'test_*.py' -v

run:
	python -m src.main
