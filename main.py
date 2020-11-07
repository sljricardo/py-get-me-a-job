import os
import requests
import shelve
from dotenv import load_dotenv
from src.Job import Job
from src.Telegram import Telegram

# Load content from .env file
load_dotenv('.env')

db           = shelve.open('store')
job_provider = requests.get('https://jobs.github.com/positions.json')
telegram     = Telegram(os.getenv("BOT_TOKEN"),os.getenv("BOT_ID"))

for work in job_provider.json():

    job = Job(work)

    if job.isValid() and job.id not in db:
        telegram.send(job.info())
        
        db[job.id] = {
            "created_at": job.created_at,
            "info": job.id
        }

db.close()