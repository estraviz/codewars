"""Human Readable Time
"""


def make_readable(seconds):
    hrs = seconds//3600
    mins = (seconds - 3600*hrs)//60
    secs = seconds - 3600*hrs - 60*mins
    return f'{hrs:02d}:{mins:02d}:{secs:02d}'
