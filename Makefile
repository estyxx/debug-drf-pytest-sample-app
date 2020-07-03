.PHONY: all clean lint test manage run
# If the first argument is "run"...
ifeq (manage,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "run"
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(RUN_ARGS):;@:)
endif


CMD:=poetry run
PYMODULE:=.
TESTS:=tests
EXTRACODE:=

all: test lint

init:
	poetry install

lint:
	@pre-commit install
	@pre-commit run --all-files
	$(CMD) pytest --dead-fixtures --dup-fixtures

run:
	$(CMD) python manage.py runserver

manage:
	$(CMD )python manage.py $(RUN_ARGS)

test:
	$(CMD) pytest --verbosity=2 --showlocals --strict --log-level=DEBUG 


clean:
	git clean -Xdf # Delete all files in .gitignore
