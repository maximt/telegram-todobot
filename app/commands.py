import json

from telegram import BotCommand, Update, User
from telegram.ext import ContextTypes

import crud
import views
from utils import strip_command, find_index_in_text


menu_commands = [
    BotCommand("add", "Add new task by /add <text>"),
    BotCommand("tsk", "Get all tasks"),
    BotCommand("rm", "Remove task by reply to it"),
]


async def add_task_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not (update.message and update.message.from_user):
        return

    try:
        task_text = strip_command(update.message.text)
        if task_text:
            user: User = update.message.from_user
            new_task = crud.create_task(user.id, task_text)
            await update.message.reply_text(
                views.new_task_view(new_task)
            )
        else:
            await update.message.reply_text(
                views.error_view('Please provide task text')
            )
    except Exception as e:
        print('Exception:', e)
        await update.message.reply_text(
            views.error_view('Sorry, something went wrong, try later please')
        )


async def get_tasks_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not (update.message and update.message.from_user):
        return

    try:
        user: User = update.message.from_user
        tasks = crud.get_tasks(user.id)
        if tasks:
            tasks_index_to_ids: dict[str, int] = {}  # map task.id for /rm command

            for index, task in enumerate(tasks, 1):
                tasks_index_to_ids[str(index)] = task.id

                await update.message.reply_text(
                    views.task_view(task, f"#{index}")
                )

                if context.user_data is not None:
                    context.user_data['tasks'] = json.dumps(tasks_index_to_ids)
        else:
            await update.message.reply_text(
                views.no_tasks_view()
            )

    except Exception as e:
        print('Exception:', e)
        await update.message.reply_text(
            views.error_view('Sorry, something went wrong, try later please')
        )


async def remove_task_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not (update.message and update.message.from_user and update.message.reply_to_message):
        return

    task_id = None

    try:
        tasks_index_to_ids: dict[str, int] = \
            json.loads(context.user_data.get('tasks', '')) \
            if context.user_data is not None else None

        if not tasks_index_to_ids:
            await update.message.reply_text(
                views.error_view('List tasks first')
            )
            return

        task_index = find_index_in_text(update.message.reply_to_message.text)
        print('task_index:', task_index)
        print('tasks_index_to_ids:', tasks_index_to_ids)
        task_id = tasks_index_to_ids.get(str(task_index), None)

        if not task_id:
            await update.message.reply_text(
                views.error_view('Reply to task')
            )
            return
    except Exception as e:
        print('Exception:', e)
        await update.message.reply_text(
            views.error_view('Sorry, something went wrong, try later please')
        )
        return

    try:
        user: User = update.message.from_user
        if crud.remove_task(user.id, task_id):
            await update.message.reply_text(
                views.remove_task_view(),
                reply_to_message_id=update.message.reply_to_message.message_id
            )
    except Exception as e:
        print('Exception:', e)
        await update.message.reply_text(
            views.error_view('Sorry, something went wrong, try later please')
        )
