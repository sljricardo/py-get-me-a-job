import requests

from JobInterface import JobInterface
from Job import Job


class WorkingNomads(JobInterface):

    def __init__(self, endpoint):
        self.response = requests.get(endpoint)
        self.jobs = []

    def info(self, offer):
        return f"""
{offer['title']}
🌍 {offer['location']} 🏢 {offer['company_name']} 🏷 {offer['category_name']}
🔗 {offer['url']}\n"""

    def getOffers(self):
        for job_offer in self.response.json():
            offer = {
                "uid": job_offer['url'],
                "content": job_offer['title'] + " " + job_offer['description']
            }

            if Job(offer).isValid():
                self.jobs.append(
                    self.info(job_offer)
                )

        return self.jobs if not None else 'No Jobs offer for ' + __name__
