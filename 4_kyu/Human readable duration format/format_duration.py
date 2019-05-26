"""Human readable duration format
"""


def format_duration(seconds):
    SEC_YEAR, SEC_DAY, SEC_HOUR, SEC_MIN = 31536000, 86400, 3600, 60
    lst_texts = []

    if seconds == 0:
        return "now"

    num_years = seconds//SEC_YEAR
    get_texts(num_years, "year", lst_texts)

    seconds = get_remaining_sec(seconds, num_years, SEC_YEAR)

    num_days = seconds//SEC_DAY
    get_texts(num_days, "day", lst_texts)

    seconds = get_remaining_sec(seconds, num_days, SEC_DAY)

    num_hours = seconds//SEC_HOUR
    get_texts(num_hours, "hour", lst_texts)

    seconds = get_remaining_sec(seconds, num_hours, SEC_HOUR)

    num_minutes = seconds//SEC_MIN
    get_texts(num_minutes, "minute", lst_texts)

    num_seconds = get_remaining_sec(seconds, num_minutes, SEC_MIN)
    get_texts(num_seconds, "second", lst_texts)

    if len(lst_texts) == 1:
        return lst_texts[0]
    elif len(lst_texts) == 2:
        return " and ".join(lst_texts)
    else:
        return ", ".join(lst_texts[:-1]) + " and " + lst_texts[-1]


def get_texts(num, time, lst):
    if num >= 1:
        txt = "{} {}".format(num, time)
        if num > 1:
            txt += "s"
        lst.append(txt)


def get_remaining_sec(sec, time, sec_time):
    return sec - time*sec_time
