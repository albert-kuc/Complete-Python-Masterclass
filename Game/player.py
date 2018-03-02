class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    """From lesson 125 - Getters and Setters"""
    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._set_lives = 0

    lives = property(_get_lives, _set_lives)

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level >= 1:
            self._level = level
            self._score = (level-1) * 1000
        else:
            print("Level cannot be less then 1")
            self._level = 1
            self._score = 0

    level = property(_get_level, _set_level)

    """From lesson 127 - Alternate Syntax for Properties"""
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    """From lesson 126 - Data Attributes and Properties"""
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)
