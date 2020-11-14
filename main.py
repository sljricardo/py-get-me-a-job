from src.JobProviders import JobProviders
from src.SenderProviders import SenderProviders
from dotenv import load_dotenv

# Add provider class Here ...
from src.providers.GitHubJobs import GitHubJobs

# Load Vars
load_dotenv()

# Register provided added Here ...
jobs = JobProviders({
    'GitHubJobs': {
        'class': GitHubJobs,
        'endpoint': 'https://jobs.github.com/positions.json'
    },
    # ....
}).getJobs()

# Send the jobs throw provider selected in .ENV
SenderProviders().send(jobs)