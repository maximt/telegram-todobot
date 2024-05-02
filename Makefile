.PHONY: all

build:
	sudo docker-compose -p demo-todo-bot build

up:
	sudo docker-compose -p demo-todo-bot up

all: build up
