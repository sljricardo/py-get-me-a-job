import abc


class SenderInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send(self):
        pass
