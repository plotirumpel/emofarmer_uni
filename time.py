class Time:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def show(self):
        return(f'{self.hours}:{self.minutes}')

    def isDay(self):
        if 12 <= self.hours < 17:
            return True
        return False

    def isMorning(self):
        if 5 <= self.hours < 12:
            return True
        return False

    def isEvening(self):
        if 17 <= self.hours <= 23:
            return True
        return False

    def isNight(self):
        if 0 <= self.hours < 5:
            return True
        return False

    def say_hello(self):
        if self.isMorning():
            return 'Доброе утро'
        if self.isDay():
            return 'Добрый день'
        if self.isEvening():
            return 'Добрый вечер'
        if self.isNight:
            return "Доброй ночи"

    def add(self, add):
        added = self.minutes + add
        self.hours += added // 60
        self.minutes = added % 60
        return self.show()
'''
t1 = Time(19,53)
print (t1.say_hello())
print(t1.add(78))
'''