from JobProviders import JobProviders
from SenderProviders import SenderProviders
from dotenv import load_dotenv

# Add provider class Here ...
from providers.GitHubJobs import GitHubJobs
from providers.WorkingNomads import WorkingNomads


def main():
    # Load Vars
    load_dotenv()

    # Register provided added Here ...
    jobs = JobProviders({
        'GitHubJobs': {
            'class': GitHubJobs,
            'endpoint': 'https://jobs.github.com/positions.json'
        },
        'WorkingNomads': {
            'class': WorkingNomads,
            'endpoint': 'https://www.workingnomads.co/api/exposed_jobs/'
        }
        # ....
    }).getJobs()

    # Send the jobs throw provider selected in .ENV
    SenderProviders().send(jobs)


if __name__ == '__main__':
    main()
