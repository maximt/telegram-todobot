import os
from dotenv import load_dotenv
load_dotenv()


required_env = [
    'TELEGRAM_TOKEN',
    'POSTGRES_HOST',
    'POSTGRES_USER',
    'POSTGRES_PASSWORD',
    'POSTGRES_DB',
]

for env in required_env:
    if not os.environ.get(env):
        msg = f"{env} is not set"
        raise ValueError(msg)
