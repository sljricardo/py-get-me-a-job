import re
import os

from DB import DB


class Job:

    def __init__(self, job):
        self.job = job
        self.allowed_words = r"php|javascript|nodejs|express|laravel|vue"
        self.denied_words = r"java$|c#|c\+\+|.net|ruby|rails|swift|Kotlin|golang|angular|react|scala|elixir"
        self.DB = DB(os.path.abspath('store'))

    def hasCorrectWords(self):
        def hasMatch(patern, string):
            return any(re.findall(patern, string, re.IGNORECASE))

        if hasMatch(self.denied_words, self.job['content']):
            return False
        if hasMatch(self.allowed_words, self.job['content']):
            return True

        return False

    def wasAlreadySended(self):
        if self.DB.hasKey(self.job['uid']):
            return True

    def isValid(self):
        if not self.wasAlreadySended() and self.hasCorrectWords():
            # Is valid, regist entry before return
            self.DB.add(self.job['uid'])
            return True

        return False
