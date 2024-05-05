Demo app.

ToDo list telegram bot.

# How to run
### Config

1. Copy .env.dist to .env
2. Open .env
3. Set you'r bot token to TELEGRAM_TOKEN

### Run

	docker-compose -p demo-todo-bot build
	docker-compose -p demo-todo-bot up

or

    make build
    make up

### Bot commands:

Create new task with *text*

    /add <text>


List all tasks

    /tsk

Remove task. Just reply to message with /rm

    /rm
