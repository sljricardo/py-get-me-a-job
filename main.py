import os
import requests
from dotenv import load_dotenv
from src.Job import Job
from src.Telegram import Telegram
from src.DB import DB

# Load content from .env file
load_dotenv('.env')

job_provider = requests.get('https://jobs.github.com/positions.json')
telegram     = Telegram(os.getenv("BOT_TOKEN"),os.getenv("BOT_ID"))
DB           = DB(os.path.abspath('store'))

for work in job_provider.json():

    job = Job(work)

    # and job.id not in db
    if job.isValid():
        if not DB.hasKey(job.id):
            telegram.send(job.info())
        
        DB.add(job.id, {
            "created_at": job.created_at,
            "info": job.id
        })

DB.close()