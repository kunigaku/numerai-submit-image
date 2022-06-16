DOCKER_IMAGE_NAME = numerai_submitter

build:
	docker build -t $(DOCKER_IMAGE_NAME) . --build-arg DISCORD_URL=$(DISCORD_URL) --build-arg NOTEBOOK_TIMEOUT=$(NOTEBOOK_TIMEOUT)

run:
	docker run --rm -it $(DOCKER_IMAGE_NAME)

help:
	@echo Hello

