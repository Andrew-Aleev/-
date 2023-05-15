class Color:
    def __init__(self, hexcode):
        self._hexcode = hexcode
        self._update_rgb()

    def _update_rgb(self):
        self._r = int(self._hexcode[0:2], 16)
        self._g = int(self._hexcode[2:4], 16)
        self._b = int(self._hexcode[4:6], 16)

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, value):
        self._hexcode = value
        self._update_rgb()

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

