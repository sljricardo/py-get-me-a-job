import shelve
import os

class DB:

    def __init__(self, file):
        self.db = shelve.open(file)

    def add(self, key, value):
        self.db[key] = value

    def hasKey(self, key):
        if os.environ.get('ENV') != 'dev':
            return True if key in self.db else False
        else:
            return False

    def close(self):
        self.db.close()
