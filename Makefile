.PHONY: help dev clean coverage check serve test test-staging test-dev superuser migrate create-db refresh-db todos token bench pytest \
		aws_ecr_update_auth_credentials aws_ecr_production_image_update aws_ecr_uat_image_update aws_eb_uat_deploy aws_eb_production_deploy \
		docker_build_local docker_build_uat docker_build_production docker_run_local

FLASK_COMMAND = flask run
FLASK_PARAMS = --debugger --reload
PYTEST_CONFIG = -s -v --cov-report  term-missing -p pytest_asyncio

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@egrep '^(.+)\:.*?#+\ *(.+)' ${MAKEFILE_LIST} | column -t -c 2 -s '#'

run: ## To run project locally
	@echo "--> \033[0;32mUping in the port 5000\033[0m"
	${FLASK_COMMAND} ${FLASK_PARAMS}

down: ## To run project locally
	@echo "--> \033[0;32mUping in the port 5000\033[0m"
	docker-compose down

build: ## To build with docker-compose
	export DOCKER_BUILDKIT=1;docker-compose build

build-no-cache:  ## To build with docker-compose and without cache
	export DOCKER_BUILDKIT=1;docker-compose build --no-cache

install-requirements:  ## To install requirements
	pip install -r requirements/base.txt

pip-compile:  ## To compile requirements
	@echo "--> \033[0;32mRemoving .txt files\033[0m"
	rm -f requirements/base.txt

	@echo "--> \033[0;32mRunning pip-compile\033[0m"
	DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose run server bash -c	"pip-compile requirements/base.in"
