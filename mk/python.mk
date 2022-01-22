.PHONY: venv
venv:	## create virtual environment using direnv
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: reqs
reqs:	# install requirements using pip
	pip install -U pip
	pip install -r requirements.txt

.PHONY: test
test:	## run tests using pytest
	pytest

.PHONY: changes
changes:	## create CHANGES file from git logs
	git log --oneline --pretty=format:"* %ad: %s" --date=short > CHANGES

.PHONY: run
run:
	python -m $(PROJECT)


