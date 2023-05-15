class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @property
    def x1(self):
        D = self._b ** 2 - 4 * self._a * self._c
        if D < 0:
            return None
        else:
            return (-self._b - D ** 0.5) / (2 * self._a)

    @property
    def x2(self):
        D = self._b ** 2 - 4 * self._a * self._c
        if D < 0:
            return None
        else:
            return (-self._b + D ** 0.5) / (2 * self._a)

    def view(self):
        return f'{self._a}x^2 + {self._b}x + {self._c}'

    def coefficients(self):
        return (self._a, self._b, self._c)




polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)

