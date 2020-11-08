import os

from dotenv import load_dotenv
from src.Telegram import Telegram
from src.JobProvider import JobProvider

# Load content from .env file
load_dotenv('.env')

jobs_providers = [
    ('gitHubJobs','https://jobs.github.com/positions.json')
]

for provider in jobs_providers:

    jobs = JobProvider(provider).getJobs()

    if jobs is not None:
        Telegram(
            os.getenv("BOT_TOKEN"),
            os.getenv("BOT_ID")
        ).send(jobs)