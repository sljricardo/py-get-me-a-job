import requests
import os

from src.DB import DB
from src.Job import Job

class JobProvider:

    def __init__(self, provider):
        self.provider, self.provider_endpoint = provider
        self.DB   = DB(os.path.abspath('store'))
        self.jobs = []

    def getJobs(self):
        jobs = requests.get(self.provider_endpoint)

        for work in jobs.json():

            job = Job(work)

            if job.isValid():
                if not self.DB.hasKey(job.id):
                    self.jobs.append(job.info())
                
                self.DB.add(job.id, {
                    "created_at": job.created_at,
                    "info": job.id
                })

        self.DB.close()
        return self.jobs