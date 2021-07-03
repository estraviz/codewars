"""What time is it?"""


def get_military_time(time):
    hour, min, sec, ampm = time[:2], time[3:5], time[6:8], time[8:10]
    if ampm == 'AM':
        hour = str(int(hour) % 12).zfill(2)
    elif ampm == 'PM':
        if hour != '12':
            hour = str(int(hour) + 12).zfill(2)
    else:
        raise Exception("Wrong time input")
    return hour + ':' + min + ':' + sec
