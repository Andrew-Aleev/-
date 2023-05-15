class HourClock:

    def __init__(self, hours):
        self._hours = hours

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        if isinstance(hours, int) and 1 <= hours <= 12:
            self._hours = hours
        else:
            raise ValueError("Некорректное время")


time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)
time = HourClock(7)

try:
    time.hours = 25
except ValueError as e:
    print(e)
