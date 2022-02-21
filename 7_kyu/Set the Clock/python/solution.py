# Set the Clock
def set_clock(time, buttons):
    hr, min = time.split(':')
    hr, min = int(hr), int(min)
    for button in buttons:
        if button == 'H':
            hr += 1
            if hr == 25:
                hr = 1
        if button == 'M':
            min += 1
    return f"{str(hr%25)}:{str(min%60).zfill(2)}"
