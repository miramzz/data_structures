
class make_month(object):
    def __init__(self, year, month):
        self.weekdays = ['Th', 'Fr', 'Sa', 'Su', 'Mo', 'Tu', 'We']
        self.special_dates = [0,3, 7, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
        self._year = year
        self._month = month
        self._anchor_days = {}

    def week_o_day(self, day):
        if not self._year in self._anchor_days:
            self._anchor_days[self._year] = self.calculate_doomsday()
        my_weekday = self.calculate_anchor_day() + self.calculate_doomsday()
        start_date = self.determine_pivot_date()
        pivot_day = self.special_dates[self._month]
        if self.is_leap_year() and (self._month == 0 or self._month ==1):
            pivot_day += 1
        if day < pivot_day :
            diff_day = pivot_day - day
            diff_day %= 7
            my_weekday -= diff_day
        else :
            diff_day = day - pivot_day
            diff_day %= 7
            my_weekday += diff_day
        my_weekday %= 7
        return self.weekdays[my_weekday]

    def is_leap_year(self):
        if self._year  % 4 and (not self._year%100 or self._year % 400):
            return True
        return False

    def determine_pivot_date(self):
        if self._month < 4 :
            return 1
        elif self._month %2 :
            return self._month
        else :
            return self._month-1

    def calculate_anchor_day(self):
        century_no = (self._year /100)
        value1 = (1+century_no) * 5
        value2 = century_no // 4
        return (value1 + value2) % 7

    def calculate_doomsday(self):
        y = self._year % 100
        value1 = y % 12
        return ((y//12) + value1 + value1//4)%7



if __name__ == "__main__":
    print make_month(2013,6).week_o_day(15) == 'Sa'
    print make_month(1969, 7).week_o_day(20) == 'Su'
    print make_month(2012, 4).week_o_day(30) == 'Mo'
    print make_month(1900, 1).week_o_day(1)  == 'Mo'
    print make_month(1789, 7).week_o_day(14) == 'Tu'

