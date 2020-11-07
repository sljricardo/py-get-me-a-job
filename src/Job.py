class Job:

    def __init__(self, job):
        self.allowed = ["php", "javascript", "nodejs", "python", "express", "laravel", "vue"]
        self.denied  = ["java", "c#", "c++", ".net", "ruby", "rails", "swift", "Kotlin", "golang", "angular", "react", "scala", "elixir"]
        self.job     = job
        self.valid   = False

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
        for allow in self.allowed:
            if allow in self.job['title'].lower() and allow in self.job['description'].lower():
                self.valid = True
                break

        for deny in self.denied:
            if deny in self.job['title'].lower() and deny in self.job['description'].lower():
                self.valid = False
                break
            
        return self.valid