import requests
import subprocess
from datetime import datetime

from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from create_main_bot import dp
from cfg.database import Database
from main_telegram_bot import Admin

db = Database('/home/str/8hab/cfg/database')


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


def main():
    Admin.register_handler_admin(dp)

    executor.start_polling(dp, on_shutdown=shutdown)


if __name__ == '__main__':
    subprocess.Popen(["/home/str/8hab/.venv/bin/python", "/home/str/8hab/telegram_bot/monitor.py"])

    main()
