import datetime



class make_month(object):
    def __init__(self, year_, month_):
        self._year = year_
        self._month = month_
        self.my_dates = ['x','Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        weekday = datetime.date(self._year, self._month, 1).weekday()
        if weekday != 0:
            for i in range(weekday):
                self.my_dates.append(self.my_dates[i+1])
            self.my_dates = self.my_dates[weekday:]


    def day(self, day_):
        return self.my_dates[day_%7]


if __name__ == "__main__":
    print make_month(2013,6).day(15) == 'Sa'
    print make_month(1969, 7).day(20) == 'Su'
    print make_month(1945, 4).day(30) == 'Mo'
    print make_month(1900, 1).day(1)  == 'Mo'
    print make_month(1789, 7).day(14) == 'Tu'

