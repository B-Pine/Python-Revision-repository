class Player(object):
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        if value >= 0:
            self._lives = value
        else:
            print("Lives cannot be less than zero")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self.score += delta * 1000
            self._level = level
        else:
            print("Level cannot be less than 1")

    # lives = property(_get_value, _set_value)
    level = property(_get_level, _set_level)

    def __str__(self):
        return (f"Name: {self.name}, Lives: {self.lives}, Score: {self.score}, "
                f"Level: {self._level}")
