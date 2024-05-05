import os

from telegram import Update
from telegram.ext import Application, CommandHandler

import settings  # noqa: F401

from commands import menu_commands, add_task_command, get_tasks_command, remove_task_command


async def post_init(application: Application) -> None:
    try:
        await application.bot.set_my_commands(commands=menu_commands)
    except Exception as e:
        print("Can't set menu commands:", e)


def main() -> None:
    token = os.environ.get("TELEGRAM_TOKEN", '')
    application = (
        Application.builder()
        .token(token)
        .post_init(post_init)
        .build()
    )

    application.add_handler(CommandHandler("add", add_task_command))
    application.add_handler(CommandHandler("tsk", get_tasks_command))
    application.add_handler(CommandHandler("rm", remove_task_command))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
