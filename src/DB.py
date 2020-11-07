import shelve

class DB:

    def __init__(self, file):
        self.db = shelve.open(file)

    def add(self, key, value):
        self.db[key] = value
        pass

    def hasKey(self, key):
        return True if key in self.db else False

    def close(self):
        self.db.close()
