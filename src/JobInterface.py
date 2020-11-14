import abc


class JobInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getOffers(self):
        pass

    @abc.abstractmethod
    def info(self):
        pass
