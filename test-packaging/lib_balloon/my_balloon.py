import abc


class Balloon:

    def __init__(self, _color, _vol):
        self.color = _color
        self.current_volume = _vol

    def pinched(self):
        self.current_volume = 0
        print("DOORRR")

    def deflated(self, _volume):
        if _volume > self.current_volume:
            return False
        else:
            self.current_volume = self.current_volume - _volume
            return True


class Flying(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def piloting(self):
        pass
