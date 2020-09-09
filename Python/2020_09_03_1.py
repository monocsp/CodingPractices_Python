# Problem : https://www.acmicpc.net/problem/2884

class Data:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @property
    def d_hour(self):
        return self.hour

    @d_hour.setter
    def d_hour(self, hour):
        self.hour = hour

    @property
    def d_minute(self):
        return self.minute

    @d_minute.setter
    def d_minute(self, minute):
        self.minute = minute


def alarmClock(hour, minute):
    if hour == 0:
        if minute < 45:
            min = minute + 60 - 45
            return Data(23, min)
        else:
            min = minute - 45
            return Data(0, min)
    else:
        if minute < 45:
            min = minute + 60 - 45
            return Data(hour - 1, min)
        else:
            min = minute - 45
            return Data(hour, min)


if __name__ == '__main__':
    h = int(input())
    m = int(input())
    data = alarmClock(h, m)
    print('{}\t{}'.format(data.d_hour, data.d_minute))
