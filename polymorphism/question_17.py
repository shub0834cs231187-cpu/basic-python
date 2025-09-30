class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def __add__(self, other):
        return Time(self.hours + other.hours, self.minutes + other.minutes)
    def __sub__(self, other):
        return Time(self.hours - other.hours, self.minutes - other.minutes)
    def __str__(self):
        return f"{self.hours}h:{self.minutes}m"

t1 = Time(2, 30)
t2 = Time(1, 45)
print(t1 + t2)
print(t1 - t2)
