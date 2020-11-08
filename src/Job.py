import re

class Job:

    def __init__(self, job):
        self.allowed_words = r"php|javascript|nodejs|express|laravel|vue"
        self.denied_words  = r"java$|c#|c\+\+|.net|ruby|rails|swift|Kotlin|golang|angular|react|scala|elixir"
        self.job     = job

    def __getattr__(self, name):
        return self.job[name]

    def info(self):
        return f"""
        **New Job Alert**\n
        **{ self.job['title'] }**\n
        **{ self.job['location'] }**\n
        **{ self.job['company'] }**\n
        [company]({ self.job['company_logo'] })\n
        [Read More]({ self.job['url'] }) """

    def isValid(self):

        hasMatch    = lambda patern, string: any(re.findall(patern, string, re.IGNORECASE))
        job_content = self.job['title'] + " " + self.job['description']

        if hasMatch(self.denied_words, job_content):
            return False

        if hasMatch(self.allowed_words, job_content):
            return True

        return False