.PHONY: quality style

check_dirs := examples src tests utils

quality:
	ruff check $(check_dirs)
	ruff format --check $(check_dirs)
	python utils/check_tests_in_ci.py

style:
	ruff check $(check_dirs) --fix
	ruff format $(check_dirs)
