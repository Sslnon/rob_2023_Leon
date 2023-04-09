class MarkerInfo:
    def __init__(self, x, y, w, h, info):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._info = info

    @property
    def pt1(self):
        return int((self._x - self._w / 2) * 640), int((self._y - self._h / 2) * 360)

    @property
    def pt2(self):
        return int((self._x + self._w / 2) * 640), int((self._y + self._h / 2) * 360)

    @property
    def center(self):
        return int(self._x * 640), int(self._y * 360)

    @property
    def text(self):
        return self._info