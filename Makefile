PYTHON ?= python3
VENV := .venv
VENV_PYTHON := $(VENV)/bin/python
MKDOCS := $(VENV)/bin/mkdocs

.DEFAULT_GOAL := help

.PHONY: help venv install serve build validate clean

help: ## Show available commands.
	@awk 'BEGIN {FS = ":.*##"}; /^[a-zA-Z_-]+:.*##/ {printf "  %-12s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

venv: ## Create the local Python virtual environment.
	@test -d $(VENV) || $(PYTHON) -m venv $(VENV)

install: venv ## Install the pinned documentation dependencies.
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PYTHON) -m pip install --requirement requirements.txt

serve: venv ## Run a live local preview at http://127.0.0.1:8000.
	$(MKDOCS) serve

build: venv ## Build the static site into site/.
	$(MKDOCS) build --strict --site-dir site

validate: build ## Build the site with strict validation.

clean: ## Remove generated site output (keeps the virtual environment).
	rm -rf site
